import sys

from nltk.corpus import brown, semcor, conll2000, treebank



CORPORA = brown, semcor, conll2000, treebank

def test_corpus_intersections(MIN=3, MAX=3):
    sets = []
    for corpus in CORPORA:
        print repr(corpus)
        a_set = set()
        counter = 0
        for a in corpus.tagged_sents():
            if MIN < len(a) <= MAX + 1 and a[-1][0] == '.':
                words = ' '.join([w[0] for w in a[:-1]])
                a_set.add(words)
                if counter < 5:
                    print words
                    sys.stdout.flush()
                    counter += 1
        sets.append((a_set, str(corpus)))

        print repr(corpus)

    for b in sets[::-1]:
        print b[1]
        print str(len(b[0])) + '\n'
        for c in sets:
            if b is not c:
                print 'with', c[1]
                d = b[0].copy()
                d = d.difference(c[0])
                print len(d)
        print '\n-------------------------------------------------------------'

