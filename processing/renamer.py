import subprocess, os, re

n = 1
f = open('connection.txt', 'w', encoding='utf-8')
f.write('new_name' + '\t' + 'old_name' + '\n')
for root, dirs, files in os.walk('C:\\Users\\Lena\\Desktop\\school_tagger\\kurs_txt_old'):
    for filename in files:
        if re.search('.txt', filename) != None:
            os.renames('C:\\Users\\Lena\\Desktop\\school_tagger\\kurs_txt_old\\' + filename, 'C:\\Users\\Lena\\Desktop\\school_tagger\\kurs_txt\\' + 'file_' + str(n) + '.txt')
            f.write('file_' + str(n) + '.txt' + '\t' + filename + '\n')
            n += 1