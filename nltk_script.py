import subprocess, os, re
from nltk.stem.snowball import RussianStemmer

for root, dirs, files in os.walk('.\\kurs_txt'):
    for filename in files:
        if re.search('\\.txt', filename) != None:
            print('file %d of %d: %s' % (files.index(filename) + 1, len(files), filename))
            f = open('kurs_txt\\' + filename, 'r', encoding = 'utf-8')
            f1 = open('kurs_txt\\' + filename[:-4] + '_stem_nltk.txt', 'w', encoding = 'utf-8')
            for line in f:
                wordsInLine = line.split()
                for word in wordsInLine:
                    word = re.sub('[^а-яёЁА-ЯA-Za-z0-9]', '', word)
                    word = word.lower()
                    f1.write(RussianStemmer(ignore_stopwords=False).stem(word) + ' ')
                f1.write('\n')

                    
            f.close()           
            f1.close()
