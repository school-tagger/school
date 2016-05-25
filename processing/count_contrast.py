'''
Скрипт считает количество словоформ в контрастной коллекции.
counter = 45154633

'''
import re
import os
import math
import csv

counter = 0

for root, dirs, files in os.walk('C:\\Users\\Lena\\Desktop\\school_tagger\\war_mystem_vopr_del'):
    for filename in files:
        if re.search('\\.txt', filename) != None:
            print('file %d of %d: %s' % (files.index(filename) + 1, len(files), filename))
            n = open('C:\\Users\\Lena\\Desktop\\school_tagger\\war_mystem_vopr_del\\' + filename, 'r', encoding = 'utf-8')
            #a = open('weirdness_mystem_' + filename, 'w', encoding = 'utf-8')
            for line in n:
                wordsInLine = line.split()
                for word in wordsInLine:
                    # word = re.sub('[^а-яёЁА-ЯA-Za-z0-9]', '', word)
                    word = word.lower()
                    counter += 1
                    
            n.close()
           
print(counter)
            
