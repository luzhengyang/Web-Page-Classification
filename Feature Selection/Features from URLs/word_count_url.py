import sys
import csv
import string
import nltk
from nltk.corpus import stopwords
from collections import Counter
reload(sys)
sys.setdefaultencoding('utf-8') 



def get_tokens(text):
	lowers = text.lower()
	no_punctuation = lowers.translate(None,string.punctuation)
	tokens = nltk.word_tokenize(no_punctuation)
	return tokens



f = open("/Users/zhengyanglu/Dropbox/Classification/profile_url.txt","r")

text = str(f.read())


tokens = get_tokens(text)
filtered = [w for w in tokens if not w in stopwords.words('english') and not w.isdigit()]
count = Counter(filtered) 
print count.most_common(100)
with open('profile_url_word_count.csv','wb+') as csvfile:
	writer = csv.writer(csvfile, dialect = 'excel')
	for i in count.most_common(100):
		writer.writerow(i)

