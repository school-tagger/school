import subprocess, os, re

f = open('help_file.txt', 'w', encoding='utf-8')
for root, dirs, files in os.walk('.\\kurs_txt'):
    for filename in files:
        if re.search('.txt', filename) != None:
            txt = r'C:\Users\Lena\Desktop\school_tagger\mystem.exe -nl ' + '\"' + filename + '\" \"' + filename[:-4] + '_lem_mystem.txt\" & echo \"' + ('file %d of %d: %s' % (files.index(filename) + 1, len(files), filename)) + '\" & '
            f.write(txt)
            #os.system(txt)
f.close()