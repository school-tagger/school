#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import re
import csv

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
        with open('pages/' + filename, 'w', encoding='utf-8') as local_file:
            local_file.write(page)
for i in range(347, 348):
    download_page('https://www.hse.ru/edu/vkr/index.html?page=' + str(i) + '&textAvailable=2')