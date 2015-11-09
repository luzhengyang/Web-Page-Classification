import sys
import os
import json
import csv
import string
import nltk
from nltk.corpus import stopwords
from collections import Counter
reload(sys)
sys.setdefaultencoding('utf-8') 



def get_tokens(text):
	lowers = text.lower()
	# no_punctuation = lowers.translate(string.punctuation)
	no_punctuation = lowers.translate({ord(k): None for k in string.punctuation})
	tokens = nltk.word_tokenize(no_punctuation)
	return tokens


filelist = ["/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta1.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta2.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta3.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta4.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta5.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta6.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta7.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta8.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta9.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta10.json"
]


filelist2 = ["/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta1.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta2.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta3.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta4.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta5.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta6.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta7.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta8.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta9.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta10.json"]


text = ""
for i in filelist2:
	f = json.load(file(i))
	for key in f.keys():
		title = f[key]["item"]["title"]
		snippet = f[key]["item"]["snippet"]
		text = text + title
		text = text + '\n'
		text = text + snippet
		text = text + '\n'


tokens = get_tokens(text)
filtered = [w for w in tokens if not w in stopwords.words('english') and not w.isdigit()]
# count = Counter(filtered) 
wordfreq = [float(filtered.count(w))/len(filtered) for w in filtered]
print wordfreq

# print str(zip(filtered, wordfreq))

# print type(count.most_common(100))
# with open('nonprofile_word_count.csv','wb+') as csvfile:
# 	writer = csv.writer(csvfile, dialect = 'excel')
# 	for i in count.most_common(100):
# 		writer.writerow(i)

