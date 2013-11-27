import cPickle as pickle
import csv
import GrammarBrain.brown_data.util.get_brown_pos_sents as gbp
from collections import Counter


def double_filter_sentence_length_histogram():
    with open('../experiment_results/sentence_length_histogram.csv', 'wb') as out_file:
        writer = csv.writer(out_file)
        for i in range(2,25):
            print i
            words_file = '../brown_pickles/sentence_words_%d.p' % i
            writer.writerow([i, len(pickle.load(open(words_file, 'rb')))])

def filter_numbers_sentence_length_histogram():
    with open('../experiment_results/numbers_sentence_length_histogram.csv', 'wb') as out_file:
        writer = csv.writer(out_file)
        for i in range(3, 26): # want a range of 2 to 24, but min is 1 less than entered,
            sentences = gbp.get_nice_sentences_as_tuples(i, i+2) # max is 2 less than entered
            print i-1, len(sentences)
            writer.writerow([i-1, len(sentences)])

def no_filters_sentence_length_histogram():
    with open('../experiment_results/raw_sentence_length_histogram.csv', 'wb') as out_file:
        writer = csv.writer(out_file)
        ss = gbp.get_brown_tagged_sentence_tuples(3,24)
        c = Counter()
        for s in ss:
            c[len(s)] += 1
        print c
        for row in sorted(c.items()):
            writer.writerow(row)

if __name__ == '__main__':
    no_filters_sentence_length_histogram()
