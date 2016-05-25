'''
Скрипт берёт на вход отлемматизированные тексты с устранёнными вариантами разбора типа "filename_mystem_vopr_del.txt" и  огромный файл с частотным списком всех триграмм для контрастной коллекции, упорядоченных по алфавиту - "weirdness_tri_conrtast.txt". Считает weirdness для триграмм. На выходе - файлы типа "weirdness_tri_wo_limit_filename_mystem_vopr_del.txt" со строками вида "триграмма:значение weirdness", упорядоченными по убыванию значения. 

Триграммы, встретившиеся в контрастной коллекции один раз, в итоговый словарь не включаются. Они обрабатываются на этапе добавления единицы.

Ограничение на частотность триграмм в тестовой коллекции отсутствует.

Кроме того, выводятся частотные списки для каждого документа из тестовой коллекции.

Входные папки и файлы: kurs_mystem_vopr_del, weirdness_tri_conrtast.txt
Выходные папки: weirdness_All_trigramms_wo_limit - значения weirdness для триграмм по документам, freqDictKursTrigrammsWeirdness - частотные списки триграмм по документам.

'''
import csv
from csv import DictWriter
import os

counter = 45154633

MegaSlovar = {}
        
y = open('C:\\Users\\Lena\\Desktop\\school_tagger\\weirdness_tri_conrtast.txt', 'r', encoding='utf-8')
reader = csv.reader(y, delimiter=':')
for row in reader:
    if int(row[1]) != 1:
        MegaSlovar[row[0]] = int(row[1])
print(len(MegaSlovar))

for root, dirs, files in os.walk('C:\\Users\\Lena\\Desktop\\school_tagger\\kurs_mystem_vopr_del'):
    for filename in files:
        # freqDictKurs = {}
        # wordsKurs = 0
        wordsAllKurs = []
        wordWeirdness = {}
        print('file %d of %d: %s' % (files.index(filename) + 1, len(files), filename))
        f = open('C:\\Users\\Lena\\Desktop\\school_tagger\\kurs_mystem_vopr_del\\' + filename, 'r', encoding='utf-8')
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
            #print(key)
            trigrammInCont = 1
            # not_breaked = True
            # for row in reader:
                # print(row)
        # if trigrammsKurs[key] > 5:
                # print(key + '--' + str(row))
            if key in MegaSlovar:
                trigrammInCont = MegaSlovar[key]
                weirdness = (int(trigrammsKurs[key]) / int(len(wordsAllKurs))) / ((int(trigrammInCont) + int(trigrammsKurs[key])) / (int(counter) + int(len(wordsAllKurs))))
                wordWeirdness[key] = weirdness
                print('нашёл!')
                # print(str(weirdness) +'= (' + str(trigrammsKurs[key]) +' / ' + str(len(wordsAllKurs)) + ') / ((' + str(trigrammInCont) + ' + ' + str(trigrammsKurs[key]) + ') / (' + str(counter) + ' + ' +  str(len(wordsAllKurs)) + '))')
                # not_breaked = False
                # break
            # if not_breaked:
            else:
                weirdness = (int(trigrammsKurs[key]) / int(len(wordsAllKurs))) / ((int(trigrammInCont) + int(trigrammsKurs[key])) / (int(counter) + int(len(wordsAllKurs))))
                wordWeirdness[key] = weirdness
                print('добавили единицу!')
            
        new = open('C:\\Users\\Lena\\Desktop\\school_tagger\\weirdness_All_trigramms_wo_limit\\' + 'weirdness_tri_wo_limit_' + filename, 'w', encoding='utf-8')        

        for word in sorted(wordWeirdness, key = lambda x: wordWeirdness[x], reverse=True):
            new.write(word + ':' + str(wordWeirdness[word]) + '\n')
        
        new.close()