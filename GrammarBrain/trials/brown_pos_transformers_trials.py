from collections import Counter

from nltk.corpus import brown
from nltk.tag.simplify import simplify_brown_tag as sbt
import nltk


def nltk_pos_tag_default():
    ''' Produces ~36 POS tags '''
    new_pos_tagged_sents = [nltk.pos_tag(sent) for sent in brown.sents()[:300]]

    ctr = Counter()

    for sent in new_pos_tagged_sents:
        for word, pos in sent:
            ctr[pos] += 1

    print len(ctr)
    return ctr

def nltk_simplify_brown_tag():
    ''' Produces ~36 POS tags '''
    other_pos_tagging = set([sbt(tag) for (_, tag) in brown.tagged_words()[:600000]])
    print len(other_pos_tagging)
    print other_pos_tagging
    return other_pos_tagging

if __name__ == '__main__':

    set2 = nltk_simplify_brown_tag()


