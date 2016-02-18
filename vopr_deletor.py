import re, os

for root, dirs, files in os.walk('.\\kurs_lem_mystem'):
    for filename in files:
        if re.search('\\.txt', filename) != None:
            f = open('.\\kurs_lem_mystem\\' + filename, 'r', encoding='utf-8')
            n = open('.\\kurs_lem_mystem\\' + filename[:-4] + '_vopr_del.txt', 'w', encoding='utf-8')
            for line in f:
                p = re.search('\\?|\\|', line)
                if p != None:
                    m = re.sub(('(\\||\\?).*?$'), '', line)
                    n.write(m)
                else:
                    n.write(line)
            f.close()
            n.close()