'''
Скрипт берёт на вход отлемматизированные тексты с устранёнными вариантами разбора типа "filename_mystem_vopr_del.txt" и считает weirdness для униграмм. На выходе -- файлы типа "weirdness_filename_mystem_vopr_del.txt" со строками вида "униграмма:значение weirdness", упорядоченными по убыванию значения. 

Установлено ограничение на частотность униграмм в тестовой коллекции: более 10.

Кроме того, выводится частотный список униграмм в контрастной коллекции и частотные списки для каждого документа из тестовой коллекции.

Входная папка: war_mystem_vopr_del - контрастная коллекция; kurs_mystem_vopr_del - тестовая коллекция.
Выходные папки: weirdness_All_unigramms - значения weirdness по документам; freqDictKurs - частотные списки по документам.
Файл freqDictWar.txt - частотный список для контрастной коллекции.

'''
import re
import os
import math
import csv

freqDictWar = {}
wordsWar = 0

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
                    if word in freqDictWar:
                            freqDictWar[word] += 1
                    else:
                        freqDictWar[word] = 1
                    wordsWar += 1
                    
            n.close()
            
y = open('freqDictWar.txt', 'w', encoding='utf-8')
for word in sorted(freqDictWar, key = lambda x: freqDictWar[x], reverse=True):
    y.write(word + ':' + str(freqDictWar[word]) + '\n')
y.write(str(wordsWar))
y.close()

for root, dirs, files in os.walk('C:\\Users\\Lena\\Desktop\\school_tagger\\kurs_mystem_vopr_del'):
    for filename in files:
        freqDictKurs = {}
        wordsKurs = 0
        wordWeirdness = {}
        f = open('C:\\Users\\Lena\\Desktop\\school_tagger\\kurs_mystem_vopr_del\\' + filename, 'r', encoding='utf-8')
        for line in f:
            wordsInLine = line.split()
            for word in wordsInLine:
                # word = re.sub('[^а-яёЁА-ЯA-Za-z0-9]', '', word)
                word = word.lower()
                if word in freqDictKurs:
                    freqDictKurs[word] += 1
                else:
                    freqDictKurs[word] = 1
                wordsKurs += 1
                
        f.close()
        
        x = open('C:\\Users\\Lena\\Desktop\\school_tagger\\freqDictKurs\\freqDictKurs_' + filename, 'w', encoding='utf-8')
        for word in sorted(freqDictKurs, key = lambda x: freqDictKurs[x], reverse=True):
            x.write(word + ':' + str(freqDictKurs[word]) + '\n')
        x.write(str(wordsKurs))
        x.close()

        for key in freqDictKurs:
            if freqDictKurs[key] > 10:
                try:
                    weirdness = (freqDictKurs[key] / wordsKurs) / ((freqDictWar[key] + freqDictKurs[key]) / (wordsWar + wordsKurs))
                    #print("weirdness = (freqDictKurs[key] / wordsKurs) / ((freqDictWar[key] + freqDictKurs[key]) / (wordsWar + wordsKurs)))")
                    wordWeirdness[key] = weirdness
                    #print(str(weirdness) +'= (' + str(freqDictKurs[key]) +' / ' + str(wordsKurs) + ') / ((' + str(freqDictWar[key]) + ' + ' + str(freqDictKurs[key]) + ') / (' + str(wordsWar) + ' + ' +  str(wordsKurs) + '))')
                    #new.write(key + ':' + str(freqDictKurs[key]) + str(weirdness) + '\n')
                except KeyError:
                    freqDictWar[key] = 1
                    weirdness = (freqDictKurs[key] / wordsKurs) / ((freqDictWar[key] + freqDictKurs[key]) / (wordsWar + wordsKurs))
                    wordWeirdness[key] = weirdness
                    #print("weirdness = (freqDictKurs[key] / wordsKurs) / ((freqDictWar[key] + freqDictKurs[key]) / (wordsWar + wordsKurs)))")
                    #print(str(weirdness) +'= (' + str(freqDictKurs[key]) +' / ' + str(wordsKurs) + ') / ((' + str(freqDictWar[key]) + ' + ' + str(freqDictKurs[key]) + ') / (' + str(wordsWar) + ' + ' +  str(wordsKurs) + '))')
                    #new.write(key + ':' + str(freqDictKurs[key]) + str(weirdness) + '\n')
                
        new = open('C:\\Users\\Lena\\Desktop\\school_tagger\\weirdness_All_unigramms\\' + 'weirdness_' + filename, 'w', encoding='utf-8')        

        for word in sorted(wordWeirdness, key = lambda x: wordWeirdness[x], reverse=True):
            new.write(word + ':' + str(wordWeirdness[word]) + '\n')
                
        new.close()
