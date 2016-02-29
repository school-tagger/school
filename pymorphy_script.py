# -!- encoding: utf-8 -!-
import pymorphy2
import re
import os

morph = pymorphy2.MorphAnalyzer()

for root, dirs, files in os.walk('.\\kurs_txt'):
    for filename in files:
        if re.search('!\\.txt', filename) != None:
            print('file %d of %d: %s' % (files.index(filename) + 1, len(files), filename))
            f = open('kurs_txt\\' + filename, 'r', encoding = 'utf-8')
            f1 = open('kurs_txt\\' + filename[:-4] + '_lem_pymorphy.txt', 'w', encoding = 'utf-8')
            for line in f:
                wordsInLine = line.split()
                for word in wordsInLine:
                    word = re.sub('[^а-яёЁА-ЯA-Za-z0-9]', '', word)
                    word = word.lower()
                    #words.append(word)
                    parsedWord = morph.parse(word)[0].normal_form
                    #m = re.sub(word, parsedWord, line)
                    f1.write(parsedWord + ' ')
                f1.write('\n')

                    
f.close()           
f1.close()

