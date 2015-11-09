#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
import string
import csv
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

path = "/Users/zhengyanglu/Dropbox/Classification/nonprofile_text"

filelist = ["/Users/zhengyanglu/Desktop/Classification/profile_text.txt"]

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

# for file in filelist:
# 	f = open(file, 'r')
# 	text = f.read()
# 	lowers = text.lower()
# 	no_punctuation = lowers.translate(None, string.punctuation)
# 	token_dict[file] = no_punctuation

for subdir, dirs, files in os.walk(path):
    for file in files:
        file_path = subdir + os.path.sep + file
        f = open(file_path,'r')
        text = f.read()
        lowers = text.lower()
        no_punctuation = lowers.translate(None,string.punctuation)
        token_dict[file] = no_punctuation


tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(token_dict.values())
# words = tfidf.get_feature_names()
weight = tfs.toarray()
print tfs
print type(weight)
print type(weight[1])
print weight[1]

test_str = "Connect with 1-800-Got-Junk MONCTON. Discuss this Deal; Call this Business Contact this Business ... Find Free Coupons Near You; Become an Affiliate"
response = tfidf.transform([test_str])
feature_names = tfidf.get_feature_names()
print type(response.nonzero()[1][1])


# for col in response.nonzero()[1]:
#     print feature_names[col], ' - ', response[0, col]

# with open('profile_tfidf.csv', 'wb+') as csvfile:
# 	writer = csv.writer(csvfile, dialect = 'excel')
# 	for i in range(len(weight)):
# 		for j in range(len(words)):
# 			writer.writerow([words[j].encode('utf-8'), weight[i][j]])
# csvfile.close()


