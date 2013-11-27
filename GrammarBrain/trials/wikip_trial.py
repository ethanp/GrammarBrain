from collections import Counter
import sys, os
file_name = '/Users/Ethan/Desktop/Data/wiki_tagged.en/englishEtiquetado_1390000_1400000'
path = '/Users/Ethan/Desktop/Data/wiki_tagged.en/'


c = Counter()
stop = 0
for file in os.listdir(path):
    if stop < 1:
        stop += 1
        print file
        with open(path+file, 'rb') as text:
            lines = text.readlines()
            if len(lines) < 3:
                break
                #continue

            print len(lines)
            for line in lines:
                if line[0] == '<':  continue
                a = line.split(' ')
                if len(a) > 2:
                    #print a[0], a[2]
                    c[a[2]] += 1
                else:
                    pass
                    #print

for b, d in c.items():
    print b

print
print len(c)
