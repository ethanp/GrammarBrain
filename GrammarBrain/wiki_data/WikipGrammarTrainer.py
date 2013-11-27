from random import random, shuffle
import time

from pybrain.datasets.classification import SequenceClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.validation import testOnSequenceData
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure.connections import FullConnection
from pybrain.structure import TanhLayer, LSTMLayer
# checkout the SharedFullConnection, LSTMLayer, BidirectionalNetwork, etc.
    # checkout whether weight sharing is a good idea
        # http://www.cs.toronto.edu/~hinton/absps/sunspots.pdf
# see if RPROP works faster

from util.wiki_pos_map import the_map
from util.get_wiki_pos_sents import get_sentence_matrices, print_sentence_range


GRAMMATICAL = (0, 1)
UNGRAMMATICAL = (1, 0)
MID_SENTENCE = (0.5, 0.5)

# if I made the interface to the Wikip data the SAME as that of the Brown data
# I could have just one class, and set Brown=True/False instead of lots of dup'd code.
# It's almost the same already, but having the pointless separation is fine for now
# as far as I'm concerned.

class WikipGrammarTrainer(object):
    #noinspection PyTypeChecker
    def __init__(self, min_len=4, max_len=5, outdim=2, hiddendim=50, train_time=50, train_set_percentage=25):
        self.MIN_LEN, self.MAX_LEN = min_len, max_len
        self.NUM_POS = len(the_map.keys())
        self.NUM_OUTPUTS, self.HIDDEN_SIZE = outdim, hiddendim
        self.network = self.build_network()
        self.training_iterations = train_time
        print str(self)
        self.TRAIN_SET_PROPORTION = float(train_set_percentage) / 100
        self.train_set, self.test_set = self.create_train_and_test_sets()

    def __str__(self):
        string = ['WIKIPEDIA DATASET']
        string += ['Sentences of length {0} to {1}'.format(str(self.MIN_LEN), str(self.MAX_LEN))]
        string += ['Hidden size: {0}'.format(str(self.HIDDEN_SIZE))]
        string += ['Number of training iterations: {0}'.format(str(self.training_iterations))]
        string += ['\n-------------------------------------------------------']
        string += ['Network Layout']
        string += ['-------------------------------------------------------']
        for module in self.network.modules:
            string += ['\n' + str(module)]
            for connection in self.network.connections[module]:
                string += [str(connection)]
        string += ['\nRecurrent connections']
        for connection in self.network.recurrentConns:
            string += [str(connection)]
        string += ['\n-------------------------------------------------------\n']
        return '\n'.join(string)


    def create_train_and_test_sets(self):

        def insert_grammatical_sequence(dataset, sentence_mat):
            dataset.newSequence()
            for i, word_vector in enumerate(sentence_mat):
                if i < len(sentence_mat) - 1:
                    dataset.appendLinked(word_vector, MID_SENTENCE)
                else:
                    dataset.appendLinked(word_vector, GRAMMATICAL)

        # there are a few options on what to do here it /would/ make sense to
        # give the first n-1 of these a `MID_SENTENCE` label like the grammatical
        # ones, but by /not/ doing that, we are assuming that we have no
        # problem declaring that partial sentences building up to ungrammatical
        # sentences should be already recognized as ungrammatical a happy
        # medium might be to label them as "probably" ungrammatical
        def insert_randomized_sequence(dataset, sentence_mat):
            dataset.newSequence()
            dup_sent_mat = sentence_mat[:]
            shuffle(dup_sent_mat)
            for word_vector in dup_sent_mat:
                dataset.appendLinked(word_vector, UNGRAMMATICAL)

        def print_data_data(data, name):
            print "num", name, "patterns: ", len(data)
            print "input and output dimensions: ", data.indim, data.outdim
            print "First sample (input, target, class):"
            print data['input'][0], data['target'][0]

        # inp: dimensionality of the input (# of POS types)
        # target: output dimensionality (# of possible classifications)
        train_data = SequenceClassificationDataSet(inp=self.NUM_POS, target=self.NUM_OUTPUTS)
        test_data = SequenceClassificationDataSet(inp=self.NUM_POS, target=self.NUM_OUTPUTS)

        print '\nFirst 2 sentences of each length', self.MIN_LEN, 'and', self.MAX_LEN
        print '------------------------------------------------------------'
        print_sentence_range(self.MIN_LEN, self.MAX_LEN)
        print '------------------------------------------------------------'
        print '\nunpickling vectorized sentences...'
        sentence_matrices = get_sentence_matrices(self.MIN_LEN, self.MAX_LEN)
        print '\ntotal number of sentences:', len(sentence_matrices)
        print 'creating training and test sets...'
        for sentence_matrix in sentence_matrices:
            # percent distribution between sets needn't be perfect, right?
            if random() < self.TRAIN_SET_PROPORTION:
                insert_grammatical_sequence(test_data, sentence_matrix)
                insert_randomized_sequence(test_data, sentence_matrix)
            else:
                insert_grammatical_sequence(train_data, sentence_matrix)
                insert_randomized_sequence(train_data, sentence_matrix)

        ''' FOR DEBUGGING DATASET '''
        print_data_data(train_data, 'training')
        print_data_data(test_data, 'testing')

        return train_data, test_data


    def build_network(self):
        network = buildNetwork(self.NUM_POS, self.HIDDEN_SIZE, self.NUM_OUTPUTS,
                         bias=True, hiddenclass=LSTMLayer, outclass=TanhLayer, recurrent=True)

        # these are the default "module" names
        # NOTE: you DO have to add a hidden->hidden connection even when you set rec=True
        #   bc otw how would it know that you wanted that /particular/ connection!?
        h = network['hidden0']
        o = network['out']

        network.addRecurrentConnection(FullConnection(o, h))

        # gets added automatically when connecting o->h for some reason
        #network.addRecurrentConnection(FullConnection(h, h))

        network.sortModules()  # must re-sort after adding new connection
        return network


    # http://pybrain.org/docs/api/supervised/trainers.html
    # backprop's "through time" on a sequential dataset
    def train(self, network_module, training_data, testing_data, n=20, s=5):
        trainer = BackpropTrainer(module=network_module, dataset=training_data, verbose=True)
        for i in range(n/s):
            trainer.trainEpochs(epochs=s)
            print 'epoch', (i+1)*s, 'finished'

            # modified from testOnClassData source code
            training_data.reset()
            print '\nTRAINING: {:.2f}% correct'.format(
                testOnSequenceData(network_module, training_data) * 100)

            print 'TESTING: {:.2f}% correct\n'.format(
                testOnSequenceData(network_module, testing_data) * 100)


    def timed_train(self, s=5):
        start = time.clock()

        self.train(network_module=self.network,
                   training_data=self.train_set, testing_data=self.test_set,
                   n=self.training_iterations, s=s)

        print '%.2f minutes' % ((time.clock() - start)/60)


if __name__ == "__main__":
    gt = WikipGrammarTrainer(train_time=2, min_len=3, max_len=3)
    gt.timed_train(s=1)
