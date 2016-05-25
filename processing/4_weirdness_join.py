'''
Скрипт объединяет уни-, би- и триграммы по каждому документу в один список, вычисляя weirdness с коэффициентами.

Входные папки: weirdness_All_unigramms - униграммы, weirdness_All_bigramms_wo_limit - биграммы, weirdness_All_trigramms_wo_limit - триграммы
Выходная папка: weirdness_uni_bi_tri

'''
import csv
import re
import os
from csv import DictWriter

for root, dirs, files in os.walk('C:\\Users\\Lena\\Desktop\\school_tagger\\weirdness_All_bigramms_wo_limit'):
    for filename2 in files:
        print('file %d of %d: %s' % (files.index(filename2) + 1, len(files), filename2))
        dict = {}
        f2 = open('C:\\Users\\Lena\\Desktop\\school_tagger\\weirdness_All_bigramms_wo_limit\\' + filename2, 'r', encoding='utf-8')
        filename1 = re.sub('bi_wo_limit_', '', filename2)
        f1 = open('C:\\Users\\Lena\\Desktop\\school_tagger\\weirdness_All_unigramms\\' + filename1, 'r', encoding='utf-8')
        filename3 = re.sub('_bi_', '_tri_', filename2)
        f3 = open('C:\\Users\\Lena\\Desktop\\school_tagger\\weirdness_All_trigramms_wo_limit\\' + filename3, 'r', encoding='utf-8')
        reader1 = csv.reader(f1, delimiter=':')
        reader2 = csv.reader(f2, delimiter=':')
        reader3 = csv.reader(f3, delimiter=':')
        # print(next(reader1)[1])
        # print(next(reader2)[1])
        # print(next(reader3)[1])
        max_uni = float(next(reader1)[1])
        if max_uni != None:
            coef2 = max_uni / float(next(reader2)[1])
            coef3 = max_uni / float(next(reader3)[1])
        else:
            print('пустая строка!')
            max_uni = 0
            coef2 = max_uni / float(next(reader2)[1])
            coef3 = max_uni / float(next(reader3)[1])
        # print(coef2)
        # print(coef3)
        for row in reader1:
            dict[row[0]] = row[1]
        for row in reader2:
            dict[row[0]] = float(row[1]) * coef2
        for row in reader3:
            dict[row[0]] = float(row[1]) * coef3
        f1.close()
        f2.close()
        f2.close()
      
        new = open('C:\\Users\\Lena\\Desktop\\school_tagger\\weirdness_uni_bi_tri\\' + 'join_' + filename1, 'w', encoding='utf-8')        
        for word in sorted(dict, key = lambda x: float(dict[x]), reverse=True):
            new.write(word + ':' + str(dict[word]) + '\n')
        new.close()

