import os
import cPickle as pickle

PICKLES = '/Users/Ethan/Dropbox/CSyStuff/ProgrammingGit/StuffIWrote/Python/GrammarBrain/GrammarBrain/brown_data/brown_pickles/'


def print_example_sentences(length, n=5):
    assert 1 < length < 25
    words_file = PICKLES+ ('sentence_words_%d.p' % length)
    if n == 1:
        print pickle.load(open(words_file, 'rb'))[0]
    else:
        print 'Length', length
        for sentence in pickle.load(open(words_file, 'rb'))[:n]:
            print sentence
        print


def print_sentence_range(MIN, MAX):
    for i in range(MIN, MAX+1):
        print_example_sentences(i, 2)


def get_sentence_matrices(MIN, MAX):
    assert 1 < MIN <= MAX < 25
    sentence_matrices = []
    for i in range(MIN, MAX+1):
        sentence_matrices += pickle.load(open(PICKLES+('sentence_matrices_%d.p' % i)))
    return sentence_matrices


if __name__ == "__main__":
    #print_sentence_range(2, 10)
    print get_sentence_matrices(2,5)
