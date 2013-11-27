# This is a test file
# it is based on
# https://github.com/kyle4211/cs165b/blob/fe02a19d54f92af797c0163b20679af93b7f5804/testpar.py
# but more related to my project, with extra help from
# pybrain/examples/neuralnets+svm/example_rnn.py

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets.classification import SequenceClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.connections import FullConnection
from pybrain.structure.modules import TanhLayer, LSTMLayer
from pybrain.tools.validation import testOnSequenceData
import sys

sds = SequenceClassificationDataSet(3, 2)
blank_label = [1./sds.outdim]*sds.outdim
grammatical_label = (0, 1)
ungrammatical_label = (1, 0)

def insert_sequence_vsn_1(the_sentence, grammatical):
    '''
    for grammatical sentences:
        label all intermediate steps as UNGRAMMATICAL

    this has the issue where if we have

        1. he went
        2. he went home
        3. he went to work

    it will end up learning that he went has P(grammatical) = 1/3, which is incorrect
    '''
    sds.newSequence()
    for i, word_vector in enumerate(the_sentence):
        if i < len(the_sentence)-1 or not grammatical:
            sds.appendLinked(word_vector, [0])

        else:
            sds.appendLinked(word_vector, [1])

def insert_sequence_vsn_3(the_sentence, grammatical):
    '''
    label all words before the end as having P(gram.) = P(ungram.) = 0.5

    '''
    sds.newSequence()
    for i, word_vector in enumerate(the_sentence):
        if grammatical:
            if i < len(the_sentence)-1:
                sds.appendLinked(word_vector, blank_label)
            else:
                sds.appendLinked(word_vector, grammatical_label)

        # there are a few options on what to do here it /would/ make sence to
        # give the first n-1 of these a `blank_label` like the grammatical
        # ones, but by /not/ doing that, we are assuming that we have no
        # problem declaring that partial sentences building up to ungrammatical
        # sentences should be already recognized as ungrammatical a happy
        # medium might be to label them as "probably" ungrammatical
        else:
            sds.appendLinked(word_vector, ungrammatical_label)

he_went = [[1, 0, 0],
           [0, 1, 0]]

blue_green = [[0, 0, 1],
              [0, 0, 1]]

he_went_blue = [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]]

happy_go = [[0, 0, 1],
            [0, 1, 0]]

sentences = [he_went, blue_green, he_went_blue, happy_go]

insert_sequence_vsn_3(he_went, True)
insert_sequence_vsn_3(blue_green, False)
insert_sequence_vsn_3(he_went_blue, True)
insert_sequence_vsn_3(happy_go, False)

print sds['input']
print sds['target']

# makes it so there are the same number of output neurons as classes
# (no longer does anything)
#sds._convertToOneOfMany()
#print 'converted:'
#print sds['target'] # now it's a (2 by n array)

# bias adds a "biasModule" on all the hidden layers
#   and if outputbias is True too, then also on the output layer
recursive_network = buildNetwork(3, 30, 2,
                         hiddenclass=LSTMLayer, outclass=TanhLayer, recurrent=True)


# does this help, and why?
recCon = FullConnection(recursive_network['out'], recursive_network['hidden0'])
recursive_network.addRecurrentConnection(recCon)

# must re-sort after adding another connection
recursive_network.sortModules()

print "------Before Training:"

def test_on_sentence(the_sentence):
    recursive_network.reset()
    for i, word in enumerate(the_sentence):
        if i < len(the_sentence)-1:
            recursive_network.activate(word)
        else:
            print recursive_network.activate(word)

print 'num_correct / len_dataset'
print testOnSequenceData(recursive_network, sds)  # what a find!


sys.stdout.flush()
trainer = BackpropTrainer(recursive_network, sds, verbose=False)
trainer.trainEpochs(500)

print "------After Training:"

for a_sentence in sentences:
    test_on_sentence(a_sentence)

print 'num_correct / len_dataset'
print testOnSequenceData(recursive_network, sds)

#print recursive_network['in']
#print recursive_network['hidden0']
#print recursive_network['out']

# modified from
# http://stackoverflow.com/questions/8150772/pybrain-how-to-print-a-network-nodes-and-weights
#for module in recursive_network.modules:
#    print '\n', module
#    for connection in recursive_network.connections[module]:
#        print connection
#        #for cc in range(len(connection.params)):
#        #    print connection.whichBuffers(cc) #, connection.params[cc]
#    if hasattr(recursive_network, "recurrentConns"):
#        print "\nRecurrent connections"
#        for connection in recursive_network.recurrentConns:
#            print connection
#            #for cc in range(len(connection.params)):
#            #    print connection.whichBuffers(cc) #, connection.params[cc]
