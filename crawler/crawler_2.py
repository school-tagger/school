#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import re
import csv
import signal

def signal_handler(signum, frame):
    raise Exception("Timed out!")

signal.signal(signal.SIGALRM, signal_handler)
signal.alarm(30)   # Ten seconds

def download_page(url):
    """Downloads page by URL and puts it into the folder
    'html_pages'"""
    print(url)

    success = True
    try:
        page = urllib.request.urlopen(url)
    except HTTPError:
        success = False
    page = page.read()
    page = page.decode("utf-8")
    filename = re.sub('/', '_', re.findall('/.*?$', url)[0])
    filename = re.sub(':', '-', filename)
    if success == True:
        with open('pages_2/' + filename, 'w', encoding='utf-8') as local_file:
            local_file.write(page)
bad_ids = []
with open('id_list.txt') as id_list:
    for line in id_list:
        line = line.strip()
        try:
            download_page('https://www.hse.ru/edu/vkr/index.html?' + line)
        except Exception:
            bad_ids.append(line)
print(bad_ids)