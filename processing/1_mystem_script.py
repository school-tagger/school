'''
Скрипт берёт на вход сырые тексты txt, лемматизирует их с помощью майстема и записывает в новые файлы вида "filename_mystem.txt"

Входная папка: kurs_txt
Выходная папка: kurs_mystem
 
'''
import subprocess, os, re

f = open('help_file.txt', 'w', encoding='utf-8')
for root, dirs, files in os.walk('C:\\Users\\Lena\\Desktop\\school_tagger\\kurs_txt'):
    for filename in files:
        if re.search('.txt', filename) != None:
            command = r'C:\\Users\\Lena\\Desktop\\other\\mystem-3.0-win7-64bit\\mystem.exe -nl ' + root + "\\" + filename + " " + re.sub("kurs_txt", "kurs_mystem", root) + "\\" + filename[:-4] + "_mystem.txt"
            f.write(command)
            # print(command)
            os.makedirs(re.sub("kurs_txt", "kurs_mystem", root), exist_ok=True)
            os.system(command)
f.close()