'''
Скрипт берёт на вход отлемматизированные тексты с устранёнными вариантами разбора типа "filename_mystem_vopr_del.txt" и считает weirdness для биграмм. На выходе -- файлы типа "weirdness_bi_wo_limit_filename_mystem_vopr_del.txt" со строками вида "биграмма:значение weirdness", упорядоченными по убыванию значения. 

Ограничение на частотность биграмм в тестовой коллекции отсутсвует.

Кроме того, выводится частотный список биграмм в контрастной коллекции и частотные списки для каждого документа из тестовой коллекции.

Входная папка: war_mystem_vopr_del - контрастная коллекция; kurs_mystem_vopr_del - тестовая коллекция.
Выходные папки: weirdness_All_bigramms_wo_limit - значения weirdness для биграмм по документам; freqDictKursBigrammsWeirdness - частотные списки для биграмм по документам.
Файл freqDictWar_bi.txt - частотный список биграмм для контрастной коллекции.

'''
import re
import os
import math
import csv

# wordsWar = 0
wordsAllWar = []

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
                    wordsAllWar.append(word)
                    # if word in freqDictWar:
                        # freqDictWar[word] += 1
                    # else:
                        # freqDictWar[word] = 1
                    # wordsWar += 1
                    
            n.close()
            
bigrammsWar = {}
n = 0
for word in wordsAllWar:
    if n != len(wordsAllWar)-1:
        bigramma = word + ' ' + wordsAllWar[n+1]
        if bigramma in bigrammsWar:
            bigrammsWar[bigramma] += 1
        else:
            bigrammsWar[bigramma] = 1
    n += 1
    
y = open('freqDictWar_bi.txt', 'w', encoding='utf-8')
for word in sorted(bigrammsWar, key = lambda x: bigrammsWar[x], reverse=True):
    y.write(word + ':' + str(bigrammsWar[word]) + '\n')
y.write(str(len(wordsAllWar)))
y.close()


for root, dirs, files in os.walk('C:\\Users\\Lena\\Desktop\\school_tagger\\kurs_mystem_vopr_del'):
    for filename in files:
        # freqDictKurs = {}
        # wordsKurs = 0
        wordsAllKurs = []
        wordWeirdness = {}
        f = open('C:\\Users\\Lena\\Desktop\\school_tagger\\kurs_mystem_vopr_del\\' + filename, 'r', encoding='utf-8')
        print('file %d of %d: %s' % (files.index(filename) + 1, len(files), filename))
        for line in f:
            wordsInLine = line.split()
            for word in wordsInLine:
                # word = re.sub('[^а-яёЁА-ЯA-Za-z0-9]', '', word)
                word = word.lower()
                wordsAllKurs.append(word)
                # if word in freqDictKurs:
                    # freqDictKurs[word] += 1
                # else:
                    # freqDictKurs[word] = 1
                # wordsKurs += 1
                
        f.close()
        
        bigrammsKurs = {}
        n = 0
        for word in wordsAllKurs:
            if n != len(wordsAllKurs)-1:
                bigramma = word + ' ' + wordsAllKurs[n+1]
                if bigramma in bigrammsKurs:
                    bigrammsKurs[bigramma] += 1
                else:
                    bigrammsKurs[bigramma] = 1
            n += 1
        
        x = open('C:\\Users\\Lena\\Desktop\\school_tagger\\freqDictKursBigrammsWeirdness\\freqDictKursBi_' + filename, 'w', encoding='utf-8')
        for word in sorted(bigrammsKurs, key = lambda x: bigrammsKurs[x], reverse=True):
            x.write(word + ':' + str(bigrammsKurs[word]) + '\n')
        x.write(str(len(wordsAllKurs)))
        x.close()

        for key in bigrammsKurs:
        #if bigrammsKurs[key] > 10:
            try:
                weirdness = (bigrammsKurs[key] / len(wordsAllKurs)) / ((bigrammsWar[key] + bigrammsKurs[key]) / (len(wordsAllWar) + len(wordsAllKurs)))
                #print("weirdness = (freqDictKurs[key] / wordsKurs) / ((freqDictWar[key] + freqDictKurs[key]) / (wordsWar + wordsKurs)))")
                wordWeirdness[key] = weirdness
                #print(str(weirdness) +'= (' + str(freqDictKurs[key]) +' / ' + str(wordsKurs) + ') / ((' + str(freqDictWar[key]) + ' + ' + str(freqDictKurs[key]) + ') / (' + str(wordsWar) + ' + ' +  str(wordsKurs) + '))')
                #new.write(key + ':' + str(freqDictKurs[key]) + str(weirdness) + '\n')
            except KeyError:
                bigrammsWar[key] = 1
                weirdness = (bigrammsKurs[key] / len(wordsAllKurs)) / ((bigrammsWar[key] + bigrammsKurs[key]) / (len(wordsAllWar) + len(wordsAllKurs)))
                wordWeirdness[key] = weirdness
                #print("weirdness = (freqDictKurs[key] / wordsKurs) / ((freqDictWar[key] + freqDictKurs[key]) / (wordsWar + wordsKurs)))")
                #print(str(weirdness) +'= (' + str(freqDictKurs[key]) +' / ' + str(wordsKurs) + ') / ((' + str(freqDictWar[key]) + ' + ' + str(freqDictKurs[key]) + ') / (' + str(wordsWar) + ' + ' +  str(wordsKurs) + '))')
                #new.write(key + ':' + str(freqDictKurs[key]) + str(weirdness) + '\n')
            
        new = open('C:\\Users\\Lena\\Desktop\\school_tagger\\weirdness_All_bigramms_wo_limit\\' + 'weirdness_bi_wo_limit_' + filename, 'w', encoding='utf-8')        

        for word in sorted(wordWeirdness, key = lambda x: wordWeirdness[x], reverse=True):
            new.write(word + ':' + str(wordWeirdness[word]) + '\n')
                
        new.close()
