from nltk.corpus import brown
from nltk.tag.simplify import simplify_brown_tag as simplify

from GrammarBrain.brown_data.util import brown_pos_map as bpm

import numpy as np

def get_medium_tagged_sentence_tuples(MIN=3, MAX=4):
    '''
    THIS FUNCTION IS NEVER USED
    Produces ~36 POS tags
    '''
    return [[(wrd, simplify(tag)) for wrd, tag in sent[:-1]] for sent in brown.tagged_sents()
                    if MIN < len(sent) <= MAX and sent[-1][0] == '.']

def get_brown_tagged_sentence_tuples(MIN=3, MAX=4):
    '''
    get sentences from the Brown dataset and their associated POS tags
    only get sentences within the specified range bounds that end in a period
    strip off the final period to simplify the overall learning task
    the sentence sizes are INCLUSIVE
    '''
    return [s[:-1] for s in brown.tagged_sents() if MIN < len(s) <= MAX and s[-1][0] == '.']

def get_nice_sentences_as_tuples(MIN=3, MAX=4, include_numbers=False, include_punctuation=False):
    ''' sentence sizes are INCLUSIVE '''
    ss = get_brown_tagged_sentence_tuples(MIN, MAX)
    if not include_numbers:
        ss = filter_numbers(ss)
    if not include_punctuation:
        ss = filter_punctuation(ss)
    return ss

def count_POSs_used(ss):  return len(set(w[1] for s in ss for w in s))

def reduce_POSs(ss):
    '''
    transform sentences
        from Brown's parts of speech (470 of them total [no joke])
        to   more 'Normal' ones      ( 12 of them total)
    '''
    return ([(word, bpm.pos_reducer[pos]) for word, pos in s] for s in ss)


def sentence_strings(ss, n=10):
    ''' print the actual sentences that were collected (without POSs) '''
    # can't do indexing on generator
    return [" ".join(w[0] for w in s) for s in ss][:n]

def filter_punctuation(ss):
    def remove_punctuation(sentence):
        for i, (word, pos) in enumerate(sentence):
            if bpm.pos_vector_index(pos) == 0: # zero means punctuation
                return False
        return True
    return filter(remove_punctuation, ss)

def filter_numbers(ss):
    def remove_numbers(sentence):
        for word, pos in sentence:
            if bpm.pos_vector_index(pos) == 11:  # eleven means number
                return False
        return True
    return filter(remove_numbers, ss)

def construct_sentence_matrices(ss, medium=False):
    '''
    takes sentences with BROWN pos tags
    returns matrices of sentences' NORMAL pos tags
    '''
    return [construct_sentence_matrix(s, medium) for s in ss]


def construct_sentence_matrix(s, medium):
    '''
    takes a sentence with BROWN pos tags
    returns matrix of sentence's NORMAL pos tags
    '''
    if medium:
        vector_len = len(bpm.medium_pos_map)
        def vector_id(the_pos):
            return bpm.medium_pos_map[simplify(the_pos)]
    else:
        vector_len = len(bpm.pos_vector_mapping)
        def vector_id(the_pos):
            return bpm.pos_vector_index(the_pos)

    sentence_matrix = []
    for _, pos in s:
        word_vector = np.zeros(vector_len)
        word_vector[vector_id(pos)] = 1
        sentence_matrix.append(word_vector)  # no [:] is necessary (I checked)
    return sentence_matrix


def print_n_sentences(ss, n=15):
    for sentence in sentence_strings(ss, n=n):
        print sentence

# for trying it out
if __name__ == "__main__":
    sentences = get_brown_tagged_sentence_tuples()[:3]
    print_n_sentences(sentences)
    matrices = construct_sentence_matrices(sentences)
    matrices2 = construct_sentence_matrices(sentences, medium=True)
