import cPickle as pickle

from GrammarBrain.brown_data.util import get_brown_pos_sents as gbp

for i in range(2, 25):
    print i
    nice_sentences = gbp.get_nice_sentences_as_tuples(MIN=i, MAX=i)
    tuple_file = 'nice_sentences_%d.p' % i
    pickle.dump(nice_sentences, open(tuple_file, 'wb'))

    sentence_matrices = gbp.construct_sentence_matrices(nice_sentences)
    matrix_file = 'sentence_matrices_%d.p' % i
    pickle.dump(sentence_matrices, open(matrix_file, 'wb'))

    sentences_words = gbp.sentence_strings(nice_sentences, 10000)
    words_file = 'sentence_words_%d.p' % i
    pickle.dump(sentences_words, open(words_file, 'wb'))
