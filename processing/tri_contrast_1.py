'''
Скрипт предобрабывает контрастную коллекцию для последующего подсчёта weirdness для триграмм. На входе -  лемматизированные тексты контрастной коллекции. На выходе - много файлов типа "freqDictWar_1"  с частотным списком триграмм, упорядоченных по алфавиту. В каждом таком файле - 500 000 строк, соответсвенно, 500 000 триграмм. В разных файлах при этом триграммы могут повторяться.

Входная папка: war_mystem_vopr_del
Выходная папка: freqDictContrast
При необходимости поменять скрипт на упорядочивание по убыванию частот и записывать в папку freqDictContrast_by_decrease.

'''
import re
import os
import math
import csv
from csv import DictWriter

# wordsWar = 0
wordsAllWar = []
trigrammsWar = {}
m = 1
k = 0

for root, dirs, files in os.walk('C:\\Users\\Lena\\Desktop\\school_tagger\\war_mystem_vopr_del'):
    for filename in files:
        if re.search('\\.txt', filename) != None:
            print('file %d of %d: %s' % (files.index(filename) + 1, len(files), filename))
            word_1 = ''
            word_2 = ''
            n = open('C:\\Users\\Lena\\Desktop\\school_tagger\\war_mystem_vopr_del\\' + filename, 'r', encoding = 'utf-8')
            #a = open('weirdness_mystem_' + filename, 'w', encoding = 'utf-8')

            for line in n:
                wordsInLine = line.split()
                for word in wordsInLine:
                    # word = re.sub('[^а-яёЁА-ЯA-Za-z0-9]', '', word)
                    word = word.lower()
                    # wordsAllWar.append(word)
                    if (word_1 != '') & (word_2 != ''):
                        trigramma = word_2 + ' ' + word_1 + ' ' + word
                    word_2 = word_1
                    word_1 = word
                    # if len(trigrammsWar) < 1000001:
                    try:
                        if trigramma in trigrammsWar:
                            trigrammsWar[trigramma] += 1
                        else:
                            trigrammsWar[trigramma] = 1
                            
                    except NameError:
                        pass
                    if len(trigrammsWar) % 1000 == 0:
                        print('%s trigrams done' % str(len(trigrammsWar) + k))
                    if len(trigrammsWar) % 500000 == 0:
                        k += 500000
                        d = open('C:\\Users\\Lena\\Desktop\\school_tagger\\freqDictContrast\\freqDictWar_' + str(m) + '.txt', 'w', encoding='utf-8')
                        for word in sorted(trigrammsWar):
                            d.write(word + ':' + str(trigrammsWar[word]) + '\n')
                        d.close()
                        m += 1
                        trigrammsWar = {}
                        

                            # trigrammsWar = {}

                    # if word in freqDictWar:
                        # freqDictWar[word] += 1
                    # else:
                        # freqDictWar[word] = 1
                    # wordsWar += 1
                    
            n.close()
            
y = open('C:\\Users\\Lena\\Desktop\\school_tagger\\freqDictContrast\\freqDictWar_' + str(m) + '.txt', 'w', encoding='utf-8')
for word in sorted(trigrammsWar):
    y.write(word + ':' + str(trigrammsWar[word]) + '\n')
# y.write(str(len(wordsAllWar)))
y.close()
            
'''
y = open('freqDictWar_tri.txt', 'a', encoding='utf-8')
reader = csv.reader(y, delimiter=':')
writer = csv.writer(y)
n = 0
m = 1
while n < len(wordsAllWar)-2:
    massivTrigramm = []
    trigrammsWar = {}
    while len(massivTrigramm) < 1000001:
        trigramma = wordsAllWar[n] + ' ' + wordsAllWar[n+1] + ' ' + wordsAllWar[n+2]
        massivTrigramm.append(trigramma)
        n +=1 
    for t in massivTrigramm:
        if t in trigrammsWar:
            trigrammsWar[t] += 1
        else:
            trigrammsWar[t] = 1
    for row in reader:
        for t in trigrammsWar:
            if row[0] == t:
                sum = int(row[1]) + trigrammsWar[t]
                trigrammsWar[t] = sum
                
    for key in sorted(trigrammsWar):
        y.write(key + ':' + str(trigrammsWar[key]) + '\n')
    print('1000000 trigrams done')
y.close()


print(len(set(massivTrigramm)))

    
for t in massivTrigramm:
    if t in trigrammsWar:
        trigrammsWar[t] += 1
    else:
        trigrammsWar[t] = 1
        
    
y = open('freqDictWar_tri.txt', 'w', encoding='utf-8')
for word in sorted(trigrammsWar, key = lambda x: trigrammsWar[x], reverse=True):
    y.write(word + ':' + str(trigrammsWar[word]) + '\n')
y.write(str(len(wordsAllWar)))
y.close()


for root, dirs, files in os.walk('C:\\Users\\Lena\\Desktop\\school_tagger\\kurs_lem_mystem_vopr_del'):
    for filename in files:
        # freqDictKurs = {}
        # wordsKurs = 0
        wordsAllKurs = []
        wordWeirdness = {}
        print('file %d of %d: %s' % (files.index(filename) + 1, len(files), filename))
        f = open('C:\\Users\\Lena\\Desktop\\school_tagger\\kurs_lem_mystem_vopr_del\\' + filename, 'r', encoding='utf-8')
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
        
        trigrammsKurs = {}
        n = 0
        for word in wordsAllKurs:
            if n < len(wordsAllKurs)-2:
                trigramma = word + ' ' + wordsAllKurs[n+1] + ' ' + wordsAllKurs[n+2]
                if trigramma in trigrammsKurs:
                    trigrammsKurs[trigramma] += 1
                else:
                    trigrammsKurs[trigramma] = 1
            n += 1
        
        x = open('C:\\Users\\Lena\\Desktop\\school_tagger\\freqDictKursTrigrammsWeirdness\\freqDictKursTri_' + filename, 'w', encoding='utf-8')
        for word in sorted(trigrammsKurs, key = lambda x: trigrammsKurs[x], reverse=True):
            x.write(word + ':' + str(trigrammsKurs[word]) + '\n')
        x.write(str(len(wordsAllKurs)))
        x.close()

        for key in trigrammsKurs:
       # if trigrammsKurs[key] > 5:
            try:
                weirdness = (trigrammsKurs[key] / len(wordsAllKurs)) / ((trigrammsWar[key] + trigrammsKurs[key]) / (len(wordsAllWar) + len(wordsAllKurs)))
                #print("weirdness = (freqDictKurs[key] / wordsKurs) / ((freqDictWar[key] + freqDictKurs[key]) / (wordsWar + wordsKurs)))")
                wordWeirdness[key] = weirdness
                #print(str(weirdness) +'= (' + str(freqDictKurs[key]) +' / ' + str(wordsKurs) + ') / ((' + str(freqDictWar[key]) + ' + ' + str(freqDictKurs[key]) + ') / (' + str(wordsWar) + ' + ' +  str(wordsKurs) + '))')
                #new.write(key + ':' + str(freqDictKurs[key]) + str(weirdness) + '\n')
            except KeyError:
                trigrammsWar[key] = 1
                weirdness = (trigrammsKurs[key] / len(wordsAllKurs)) / ((trigrammsWar[key] + trigrammsKurs[key]) / (len(wordsAllWar) + len(wordsAllKurs)))
                wordWeirdness[key] = weirdness
                #print("weirdness = (freqDictKurs[key] / wordsKurs) / ((freqDictWar[key] + freqDictKurs[key]) / (wordsWar + wordsKurs)))")
                #print(str(weirdness) +'= (' + str(freqDictKurs[key]) +' / ' + str(wordsKurs) + ') / ((' + str(freqDictWar[key]) + ' + ' + str(freqDictKurs[key]) + ') / (' + str(wordsWar) + ' + ' +  str(wordsKurs) + '))')
                #new.write(key + ':' + str(freqDictKurs[key]) + str(weirdness) + '\n')
            
        new = open('C:\\Users\\Lena\\Desktop\\school_tagger\\weirdness_All_trigramms_wo_limit\\' + 'weirdness_tri_wo_limit_' + filename, 'w', encoding='utf-8')        

        for word in sorted(wordWeirdness, key = lambda x: wordWeirdness[x], reverse=True):
            new.write(word + ':' + str(wordWeirdness[word]) + '\n')
                
        new.close()
'''