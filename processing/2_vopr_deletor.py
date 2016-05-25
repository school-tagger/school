'''
Скрипт берёт на вход файлы вида "filename_mystem.txt" с лемматизированными текстами и избавляется от вариантов, возникших при лемматизации, оставляя только перый вариант как наиболее вероятный. Также удаляются вопросительные знаки, возникшие при разборе. На выходе - файлы вида "filename_mystem_vopr_del.txt"

Входная папка: kurs_mystem
Выходная папка: kurs_mystem_vopr_del
'''
import re, os

for root, dirs, files in os.walk('C:\\Users\\Lena\\Desktop\\school_tagger\\kurs_mystem'):
    for filename in files:
        if re.search('\\.txt', filename) != None:
            f = open('C:\\Users\\Lena\\Desktop\\school_tagger\\kurs_mystem\\' + filename, 'r', encoding='utf-8')
            n = open('C:\\Users\\Lena\\Desktop\\school_tagger\\kurs_mystem_vopr_del\\' + filename[:-4] + '_vopr_del.txt', 'w', encoding='utf-8')
            for line in f:
                p = re.search('\\?|\\|', line)
                if p != None:
                    m = re.sub(('(\\||\\?).*?$'), '', line)
                    n.write(m)
                else:
                    n.write(line)
            f.close()
            n.close()