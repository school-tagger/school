#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import re
import os
import csv


idss = []

for root, dirs, files in os.walk('./pages_2/'):
	for name in files:
		print(os.path.join(root, name))
		with open(os.path.join(root, name)) as page:
			#a = page.readlines()
			for line in page:
				#line.decode('utf-8')
				ids = re.findall('<a href=\"(.*?)\">Текст работы</a>', line)
				if len(ids) > 0:
					for i in ids:
						idss.append([i, os.path.join(root, name)])

with open('doc_list.txt', 'w') as id_list:
	for j in idss:
		id_list.write(j[0] + '\t' + j[1] + '\n')