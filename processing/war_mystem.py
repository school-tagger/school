import os
import re

for root, dirs, files in os.walk('C:\\Users\\Lena\\Desktop\\school_tagger\\war'):
    for filename in files:
        command = "C:\\Users\\Lena\\Desktop\\other\\mystem-3.0-win7-64bit\\mystem.exe -nl " + root + "\\" + filename + " " + re.sub("war", "war_mystem", root) + "\\" + filename[:-4] + "_mystem.txt"
        
        print(command)
        os.makedirs(re.sub("war", "war_mystem", root), exist_ok=True)
        os.system(command)