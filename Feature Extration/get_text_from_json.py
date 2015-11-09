# -*- coding: utf-8 -*-
import sys
import json
import csv


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


def write_to_individual_file(filelist):
	j = 1
	for i in filelist:
		text = []
		f = json.load(file(i))
		for key in f.keys():
			title = f[key]["item"]["title"].encode("utf8")
			snippet = f[key]["item"]["snippet"].encode("utf8")
			text.append(title)
			text.append('\n')
			text.append(snippet)
			text.append('\n')
			with open('profile_text_'+str(j)+'.txt','w+') as p:
				for line in text:
					p.writelines(line)
			j+=1

def write_to_excel(filelist):
	for i in filelist:
		f = json.load(file(i))
		for key in f.keys():
			title = f[key]["item"]["title"].encode("utf8")
			snippet = f[key]["item"]["snippet"].encode("utf8")
			text = title + ' ' + snippet
			with open('profile_text_excel.csv','ab') as csvfile:
				writer = csv.writer(csvfile, dialect='excel')
				writer.writerow([text,'Profile'])



# with open('nonprofile_text.txt','w+') as f:
# 	for line in text:
# 		f.writelines(line)


def main():
	write_to_excel(filelist)

if __name__ == '__main__':
	sys.exit(main())


