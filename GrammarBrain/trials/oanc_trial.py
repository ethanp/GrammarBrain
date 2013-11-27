from lxml import etree


sample_file = '/Users/Ethan/Desktop/Data/OANC-GrAF/data/written_1/journal/slate/6/Article247_702-hepple.xml'
with open(sample_file, 'rb') as xml_binary:
    tree = etree.parse(xml_binary)

root = tree.getroot()
sentences = []
sentence = []
for child in root:
    if child.tag[-1] == 'a':
        for b in child:
            # these are the fs-s
            word = None
            pos = None
            for c in b:
                # need those whose name is "msd" for the POS tag.
                if c.get('name') == 'base':
                    word = c.get('value')
                if c.get('name') == 'msd':
                    pos = c.get('value')
            if word and pos:
                sentence.append((word, pos))
                if pos == '.':
                    to_add = sentence[:]
                    sentences.append(to_add)
                    sentence = []
            else:
                raise Exception('no word and pos')

print len(sentences)
print
for s in sentences:
    print len(s)
