import cPickle as pickle
import pickle_wikip

def print_example_sentences(length, n=2):
    '''
    print TEXT of @n sentences of length @length from wiki corpus
    '''
    assert 1 < length < 25
    pass

def print_sentence_range(MIN, MAX):
    '''
    from MIN to MAX -> INCLUSIVE OF BOTH
    '''
    assert MIN <= MAX
    pass

def get_sentence_matrices(MIN, MAX):
    '''
    from MIN to MAX -> INCLUSIVE OF BOTH
    '''
    assert 1 < MIN <= MAX < 25
    matrices = []
    for i in range(MIN, MAX+1):
        filename = pickle_wikip.matrix_file_of_len + str(i) + '.p'
        unpickled_matrices = pickle.load(open(filename, 'rb'))
        print 'sentence length', i
        print 'len(unpickled_matrices)', len(unpickled_matrices)
        matrices += unpickled_matrices
    return matrices


if __name__ == '__main__':
    print get_sentence_matrices(3,3)[0][0]
