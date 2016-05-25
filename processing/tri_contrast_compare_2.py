'''
Скрипт пробегает по всем файлам с частотными списками триграмм для контрастной коллекции и складывает значения у совпадающих. На вход - файлы с частотными списками триграмм типа "freqDictWar_1", упорядоченных по алфавиту, на выходе - огромный файл с частотным списком всех триграмм для контрастной коллекции, упорядоченных по алфавиту - "weirdness_tri_conrtast.txt". В нём триграммы уже не повторяются.

Входная папка: freqDictContrast
Выходной файл: weirdness_tri_conrtast.txt

'''
import csv
import re
import os
from csv import DictWriter

def empty_triplet(listOfTriplets):
    for triplet in listOfTriplets:
        if triplet != []:
            return True
        
listOfTriplets = []
BigDict = {}
for root, dirs, files in os.walk('C:\\Users\\Lena\\Desktop\\school_tagger\\freqDictContrast'):
    for filename in files:
        print('file %d of %d: %s' % (files.index(filename) + 1, len(files), filename))
        f = open('C:\\Users\\Lena\\Desktop\\school_tagger\\freqDictContrast\\' + filename, 'r', encoding='utf-8')
        reader = csv.reader(f, delimiter=':')
        BigDict[filename] = reader
        
for i in BigDict:
    triplet = []
    triplet.append(i)
    for row in BigDict[i]:
        trigramma = row[0]
        numberOfOccurences = row[1]
        triplet.append(trigramma)
        triplet.append(numberOfOccurences)
        listOfTriplets.append(triplet)
        break
       
y = open('C:\\Users\\Lena\\Desktop\\school_tagger\\weirdness_tri_conrtast.txt', 'w', encoding='utf-8')

n = 0
while empty_triplet(listOfTriplets) == True:
    trigrams = []
    sum = 0
    for triplet in listOfTriplets:
        trigrams.append(triplet[1])

    min = sorted(trigrams)[0]

    for triplet in listOfTriplets:
        if triplet[1] == min:
            sum = sum + int(triplet[2])
            try:
                newRow = next(BigDict[triplet[0]])
                triplet[1] = newRow[0]
                triplet[2] = newRow[1]
            except StopIteration:
                triplet[0] = ''
                triplet[1] = ''
                triplet[2] = ''
    y.write(min + ':' + str(sum) + '\n')
    n += 1
    if n % 10000 == 0:
        try:
            print(str(n) + ' trigrams done')
            print(min + ':' + str(sum))
        except UnicodeDecodeError:
            print(str(n) + ' trigrams done')
            print('foo' + ':' + str(sum))
            
y.close()

