# -!- encoding: utf-8 -!-
import os, re

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.datasets import fetch_20newsgroups
from sklearn.cluster import KMeans
from optparse import OptionParser
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
import nltk

import numpy as np

categories = None

dataset = fetch_20newsgroups(subset='all', categories=categories,
                             shuffle=True, random_state=42)
#print(dataset)

labels = dataset.target
#for label in labels:
#    print(label)
true_k = np.unique(labels).shape[0]
print(true_k)

transformer = TfidfTransformer()

num_clusters = 10

km = KMeans(n_clusters=num_clusters)

#stopwords = nltk.corpus.stopwords('russian')

op = OptionParser()

(opts, args) = op.parse_args()



def read_file(filename):
    f = open('.\\kurs_lem_pymorphy\\' + filename, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    return text

    
#stopwords = ['и', 'о', 'в', 'а', 'с', 'он', 'из', 'ил', 'эт', 'по', 'на', 'не', 'для', 'что', 'как', 'так', 'от', 'но']
stopwords = ['и', 'о', 'в', 'а', 'с', 'он', 'из', 'или', 'это', 'по', 'на', 'не', 'для', 'что', 'как', 'так', 'от', 'но', 'то', 'быть', 'мы', 'они', 'она', 'этот', 'который', 'весь', 'при', 'за']
vectorizer = CountVectorizer(min_df=1, stop_words=stopwords)

corpus = []
filenames = []
labels2 = ['journ', 'ling', 'philol', 'comp_sc', 'juro', 'journ2', 'ling2', 'philol2', 'comp_sc2', 'juro2']
for root, dirs, files in os.walk('.\\kurs_lem_pymorphy'):
    for filename in files:
        if re.search('\\.txt', filename) != None:
            filenames.append(filename)
            print(filename)
            a = read_file(filename)
            corpus.append(a)
            
true_k = np.unique(labels2).shape[0]
#corpus = [read_file('!Chenina2009!_stem_nltk.txt'), read_file('Privoznov_diplom_2014_stem_nltk.txt'), read_file('kochetova_ov_programma-sinhronizacii-dvijeniy-robotov-nao_10091_stem_nltk.txt'), read_file('Kursovaya_Sokolov_SSP-217_stem_nltk.txt'), read_file('3_kurs_r_o_kursovaya_22Saga_s_pomarkami_22_T_A_Bek_stem_nltk.txt')]

X = vectorizer.fit_transform(corpus)

n = open('output.txt', 'w', encoding='utf-8')
n.write(str(X.toarray()))


counts = X.toarray()
tfidf_matrix = transformer.fit_transform(counts)
print(tfidf_matrix.toarray())

km.fit(tfidf_matrix)

clusters = km.labels_.tolist()

n.write('\n')
n.write(str(clusters))
i = 0
for cl in clusters:
    print(cl)
    print(filenames[i])
    n.write('\n%d - %s' % (cl, filenames[i]))
    i += 1
    

'''
print("Top terms per cluster:")
print()
#sort cluster centers by proximity to centroid
order_centroids = km.cluster_centers_.argsort()[:, ::-1] 




for i in range(num_clusters):
    print("Cluster %d words:" % i, end='')
    
    for ind in order_centroids[i, :6]: #replace 6 with n words per cluster
        print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
    print() #add whitespace
    print() #add whitespace
    
    print("Cluster %d titles:" % i, end='')
    for title in frame.ix[i]['title'].values.tolist():
        print(' %s,' % title, end='')
    print() #add whitespace
    print() #add whitespace
    
print()
print()
''' 
#if opts.n_components:
#original_space_centroids = svd.inverse_transform(km.cluster_centers_)
#order_centroids = original_space_centroids.argsort()[:, ::-1]
#else:
order_centroids = km.cluster_centers_.argsort()[:, ::-1]

terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i, end='')
    n.write("\nCluster %d:" % i)
    for ind in order_centroids[i, :10]:
        #print(' %s' % terms[ind], end='')
        n.write(' %s' % terms[ind])
    print()
n.close()