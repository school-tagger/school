import re
import os
import math

freqdict = {}
wordsAll = []
bigramms = {}
a = open('freq_list.txt', 'w', encoding = 'utf-8')
for root, dirs, files in os.walk('.\\kurs_stem_nltk'):
    for filename in files:
        if re.search('\\.txt', filename) != None:
            print('file %d of %d: %s' % (files.index(filename) + 1, len(files), filename))
            f = open('kurs_stem_nltk\\' + filename, 'r', encoding = 'utf-8')
            for line in f:
                wordsInLine = line.split()
                for word in wordsInLine:
                    word = re.sub('[^а-яёЁА-ЯA-Za-z0-9]', '', word)
                    word = word.lower()
                    wordsAll.append(word)
                    if word in freqdict:
                            freqdict[word] += 1
                    else:
                        freqdict[word] = 1
            #print(wordsAll)
            n = 0

            f.close()
for word in wordsAll:
    if n != len(wordsAll)-1:
        bigramma = word + ' ' + wordsAll[n+1]
        if bigramma in bigramms:
            bigramms[bigramma] += 1
        else:
            bigramms[bigramma] = 1
    n += 1
b = open('bigramms.txt', 'w', encoding = 'utf-8')
mi_file = open('mi.txt', 'w', encoding = 'utf-8')
MI_dict = {}
for bigramma in sorted(bigramms, key = lambda x: bigramms[x], reverse=True):
    f1 = freqdict[re.findall('\w+\s', bigramma)[0][:-1]]
    f2 = freqdict[re.findall('\s\w+', bigramma)[0][1:]]
    mi = math.log2((bigramms[bigramma] * 152328)/(f1 * f2))
    if bigramms[bigramma] > 39:
        MI_dict[bigramma] = mi
    b.write(bigramma + ':' + str(bigramms[bigramma]) + ' MI: ' + str(mi) + '\n')

b.close()

for bigramma in sorted(MI_dict, key = lambda x: MI_dict[x], reverse=True):
    mi_file.write(bigramma + ':' + str(MI_dict[bigramma]) + '\n')
    
for word in sorted(freqdict, key = lambda x: freqdict[x], reverse=True):
    a.write(word + ':' + str(freqdict[word]) + '\n')

a.close()


