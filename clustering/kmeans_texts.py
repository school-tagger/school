#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

documents = []
document_names = []


stop_words_list = []
with open('stop-words.txt') as stop_words:
	for line in stop_words:
		stop_words_list.append(line.strip())

for root, dirs, files in os.walk('./kurs_mystem_vopr_del/'):
	for name in files:
		documents.append("")
		document_names.append(name)
		with open(os.path.join(root, name)) as doc:
			for line in doc:
				documents[-1] += line.strip() + ' '

vectorizer = TfidfVectorizer(stop_words=stop_words_list)
X = vectorizer.fit_transform(documents)

true_k = 20
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1, verbose=2)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print "Cluster %d:" % i,
    for ind in order_centroids[i, :10]:
        print ' %s' % terms[ind],
    print
print model.labels_

with open("model.csv", "w") as out_file:
	for i in model.labels_:
		out_file.write(document_names[model.labels_.index(i)] + ',' + model.labels_.index(i) + '\n')