#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import re
import csv
import signal
'''
def signal_handler(signum, frame):
    raise Exception("Timed out!")

signal.signal(signal.SIGALRM, signal_handler)
signal.alarm(30)   # Ten seconds
'''
def download_page(url):
    """Downloads page by URL and puts it into the folder
    'html_pages'"""
    print(url)

    success = True
    try:
        urllib.request.urlretrieve('https://www.hse.ru' + urllib.parse.quote(url), 'files/' + re.sub('/', '_', re.findall('/.*?$', url)[0]))
    except urllib.error.HTTPError:
        return url

bad_ids = []
with open('doc_list.txt') as doc_list:
    doc_reader = csv.reader(doc_list, delimiter='\t')
    for row in doc_reader:
        bad_ids.append(download_page(row[0]))

with open('404.txt', 'w') as not_found:
    for i in bad_ids:
        not_found.write(i + '\n')