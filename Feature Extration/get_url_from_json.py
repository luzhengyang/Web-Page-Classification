'''
Extract URL from json
'''
import sys
import json
from spliturl import split_url
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
import csv
from urlparse import urlparse

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
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta10.json"
]


def write_to_file(filelist):
	urls = []
	for i in filelist:
		f = json.load(file(i))
		for key in f.keys():
			urls.append(f[key]["item"]["url"].encode('utf8'))
	with open('profile_url.txt','w+') as p:
		for url in urls:
			o = urlparse(url)
			if o.path is not None:
				tokens = split_url(o.path)
				for token in tokens:
					p.writelines(token+' ')
				p.writelines('\n')

def write_to_excel(filelist):
	for i in filelist:
		f = json.load(file(i))
		for key in f.keys():
			url = f[key]["item"]["url"].encode('utf8')
			splited_url = split_url(url)
			text = ' '.join(splited_url)
			with open('profile_url_excel.csv','ab') as csvfile:
				writer = csv.writer(csvfile, dialect='excel')
				writer.writerow([text,'Profile'])

def main():
	write_to_excel(filelist)

if __name__ == '__main__':
	sys.exit(main())