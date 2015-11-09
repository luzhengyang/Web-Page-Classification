#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
import string
import csv

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer


filelist = ["/Users/zhengyanglu/Desktop/Classification/search_url.txt"]

token_dict = {}
stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

for file in filelist:
	f = open(file, 'r')
	text = f.read()
	lowers = text.lower()
	no_punctuation = lowers.translate(None, string.punctuation)
	token_dict[file] = no_punctuation

tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(token_dict.values())
words = tfidf.get_feature_names()
weight = tfs.toarray()

with open('search_url_tfidf.csv', 'wb+') as csvfile:
	writer = csv.writer(csvfile, dialect = 'excel')
	for i in range(len(weight)):
		for j in range(len(words)):
			writer.writerow([words[j].encode('utf-8'), weight[i][j]])
csvfile.close()


