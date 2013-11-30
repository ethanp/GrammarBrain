import cPickle as pickle
import csv
from random import shuffle
from pybrain.datasets import SequenceClassificationDataSet
from GrammarBrain.brown_data.util.brown_pos_map import pos_vector_mapping, medium_pos_map
from GrammarBrain.brown_data.util.get_brown_pos_sents import get_nice_sentences_as_tuples, construct_sentence_matrices
from GrammarBrain.brown_data.util.my_seq_tester import testOnSequenceData

PATH = '/Users/Ethan/Dropbox/CSyStuff/GrammarBrain/GrammarBrain/brown_data/experiment_results/Gen Error 4 to 8/'
PICKLE = 'part_2_11:29-21:22.p'
PICKLE_2 = 'part_4_11:30-11:21.p'
OUT_CSV = 'extension.csv'

GRAMMATICAL = (0, 1)
UNGRAMMATICAL = (1, 0)
MID_SENTENCE = (0.5, 0.5)

def insert_grammatical_sequence(dataset, sentence_mat):
    dataset.newSequence()
    for i, word_vector in enumerate(sentence_mat):
        if i < len(sentence_mat) - 1:
            dataset.appendLinked(word_vector, MID_SENTENCE)
        else:
            dataset.appendLinked(word_vector, GRAMMATICAL)

# there are a few options on what to do here it /would/ make sense to
# give the first n-1 of these a `blank_label` like the grammatical
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

def generalization_error(net, length, inp_len, med, numb, punct):
    sentence_tuples = get_nice_sentences_as_tuples(MIN=length, MAX=length,
                                                   include_numbers=numb,
                                                   include_punctuation=punct)

    exper_data = SequenceClassificationDataSet(inp=inp_len, target=2)

    sentence_matrices = construct_sentence_matrices(sentence_tuples, medium=med)
    for s in sentence_matrices:
        insert_grammatical_sequence(exper_data, s)
        insert_randomized_sequence(exper_data, s)

    return 1 - testOnSequenceData(net, exper_data)

def first_vsn():
    print 'loading network'
    loaded_network = pickle.load(open(PATH+PICKLE, 'rb'))
    print 'loaded network'

    with open(PATH+OUT_CSV, 'wb') as output:
        writer = csv.writer(output)
        for sentence_len in range(20, 30):
            print 'error on len:', sentence_len
            gen_error = generalization_error(loaded_network, sentence_len, len(pos_vector_mapping), False, True, True)
            error_at_len = ['Generalization Error', sentence_len, gen_error]
            writer.writerow(error_at_len)
            print error_at_len

def second_version():
    print 'loading network'
    loaded_network = pickle.load(open(PATH+PICKLE, 'rb'))
    print 'loaded network'

    with open(PATH+'ext_2.csv', 'wb') as output:
        writer = csv.writer(output)
        for sentence_len in range(20, 30):
            print 'error on len:', sentence_len
            gen_error = generalization_error(loaded_network, sentence_len, len(pos_vector_mapping), False, False, False)
            error_at_len = ['Generalization Error', sentence_len, gen_error]
            writer.writerow(error_at_len)
            print error_at_len

def third_version():
    print 'loading network'
    loaded_network = pickle.load(open(PATH+PICKLE_2, 'rb'))
    print 'loaded network'

    with open(PATH+'ext_3.csv', 'wb') as output:
        writer = csv.writer(output)
        for sentence_len in range(5, 30):
            print 'error on len:', sentence_len
            gen_error = generalization_error(loaded_network, sentence_len, len(medium_pos_map), True, False, False)
            error_at_len = ['Generalization Error', sentence_len, gen_error]
            writer.writerow(error_at_len)
            print error_at_len

if __name__ == '__main__':
    third_version()
