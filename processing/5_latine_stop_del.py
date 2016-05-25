# -*- coding: utf-8 -*-
'''
Скрипт принимает на вход файлы со списками ключевых слов, упорядоченных по убыванию значения weirdness. Удаляет ключевые слова, в которых содержатся стоп-слова и / или латиница.

Входная папка: weirdness_uni_bi_tri
Выходная папка: weirdness_uni_bi_tri_clean

'''
import csv
import re
import os
from csv import DictWriter

stop = set(['а', 'е', 'и', 'ж', 'м', 'о', 'на', 'не', 'ни', 'об', 'но', 'он', 'мне', 'мои', 'она', 'они', 'оно', 'мной', 'мой', 'можно', 'мочь', 'над', 'нее', 'оба', 'мимо', 'надо', 'наиболее', 'между', 'нибудь', 'никогда', 'никуда', 'нет', 'ничего', 'несколько', 'опять', 'около', 'мы', 'ну', 'от', 'отовсюду', 'нужно', 'очень', 'отсюда', 'в', 'во', 'вон', 'вот', 'ведь', 'ваш', 'весь', 'вдруг', 'вы', 'все', 'всегда', 'всё', 'г', 'год', 'где', 'да', 'ее', 'за', 'из', 'ли', 'же', 'до', 'по', 'под', 'пожалуйста', 'пока', 'пора', 'потом', 'потому', 'после', 'почему', 'почти', 'посреди', 'ей', 'или', 'без', 'даже', 'алло', 'для', 'лет', 'зато', 'перед', 'затем', 'зачем', 'лишь', 'бы', 'еще', 'при', 'про', 'просто', 'если', 'будто', 'ещё', 'к', 'конечно', 'когда', 'который', 'кем', 'каждый', 'кажется', 'как', 'какой', 'кто', 'кроме', 'куда', 'с', 'т', 'у', 'я', 'уж', 'со', 'то', 'снова', 'совсем', 'тогда', 'тоже', 'собой', 'тобой', 'сначала', 'только', 'тот', 'хоть', 'хотя', 'твой', 'раз', 'уже', 'сам', 'там', 'тем', 'чем', 'сейчас', 'чего', 'себе', 'тебе', 'разве', 'теперь', 'себя', 'тебя', 'так', 'такой', 'через', 'часто', 'сколько', 'ты', 'что', 'это', 'чтоб', 'чтобы', 'этот', 'туда', 'рядом', 'тут', 'чуть'])
for root, dirs, files in os.walk('C:\\Users\\Lena\\Desktop\\school_tagger\\weirdness_uni_bi_tri'):
    for filename in files:
        print('file %d of %d: %s' % (files.index(filename) + 1, len(files), filename))
        newGramms = {}
        n = open('C:\\Users\\Lena\\Desktop\\school_tagger\\weirdness_uni_bi_tri\\' + filename, 'r', encoding = 'utf-8')
        reader = csv.reader(n, delimiter=':')
        for row in reader:
            # print(row)
            badWord = False
            wordsInLine = row[0].split()
            for word in wordsInLine:
                if word in stop:
                    # print(word + 'in' + row[0] + ' -- стоп-слово!')
                    badWord = True
                elif re.search('[^а-яёЁА-Я]', word) != None:
                    # print(word + 'in' + row[0] + ' -- латиница!')
                    badWord = True
            if badWord == False:
                newGramms[row[0]] = row[1]
            
        x = open('C:\\Users\\Lena\\Desktop\\school_tagger\\weirdness_uni_bi_tri_clean\\' + 'join_clean_' + filename, 'w', encoding='utf-8')
        for word in sorted(newGramms, key = lambda x: float(newGramms[x]), reverse=True):
            x.write(word + ':' + str(newGramms[word]) + '\n')
        x.close()
        
print(newGramms)

                
                    
                
 
