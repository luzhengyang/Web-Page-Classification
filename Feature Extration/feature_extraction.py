import sys
import csv
import json
from urlparse import urlparse
from bag_of_words import bag_of_words
from hasTargetBusinessName import has_target_business_name_in_text, has_target_business_name_in_domain
from hasPhoneNumber import has_phone_number
from hasCity import has_city
from hasTargetCity import has_target_city
from hasDirectoryProvider import has_directory_provider
from hasReviewProvider import has_review_provider
from hasZipcode import has_zip_code
from hasStreetType import has_street_type
from hasRegion import has_region
reload(sys)
sys.setdefaultencoding('utf-8') 



# filelist = ["/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta1.json",
# "/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta2.json",
# "/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta3.json",
# "/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta4.json",
# "/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta5.json",
# "/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta6.json",
# "/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta7.json",
# "/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta8.json",
# "/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta9.json",
# "/Users/zhengyanglu/Dropbox/Classification/Profile/resultMeta10.json"]

filelist = ["/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta1.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta2.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta3.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta4.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta5.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta6.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta7.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta8.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta9.json",
"/Users/zhengyanglu/Dropbox/Classification/Profile/nonprofile_resultItemsMeta10.json"]

def main():
	
	dictlist = []

	for f in filelist:
		# featurelist = []
		pages = json.load(file(f))

		for key in pages.keys():
			if key != "resultItemCount":
				businessName = pages[key]["businessName"]
				targetCity = pages[key]["city"]
				title = pages[key]["item"]["title"]
				snippet = pages[key]["item"]["snippet"]
				title_snippet = title + "\n" + snippet
				url = pages[key]["item"]["url"]
				o = urlparse(url)
				domain = o.netloc
				# rest = o.path

				# bow = bag_of_words(title_snippet)
				business_name_domain = has_target_business_name_in_domain(businessName,domain)
				business_name_text = has_target_business_name_in_text(businessName,title_snippet)
				phone_number = has_phone_number(title_snippet)
				city = has_city(title_snippet)
				region = has_region(title_snippet)
				target_city = has_target_city(targetCity,title_snippet)
				directory_provider = has_directory_provider(domain)
				review_provider = has_review_provider(domain)
				zip_code = has_zip_code(title_snippet)
				street_type = has_street_type(title_snippet)

				dict1 = dict(region, **business_name_domain)
				dict2 = dict(dict1, **business_name_text)
				dict3 = dict(dict2, **phone_number)
				dict4 = dict(dict3, **city)
				dict5 = dict(dict4, **target_city)
				dict6 = dict(dict5, **directory_provider)
				dict7 = dict(dict6, **review_provider)
				dict8 = dict(dict7, **zip_code)
				dict9 = dict(dict8, **street_type)
				dictlist.append(dict9)

				
	with open('nonprofile_features.csv','wb+') as csvfile:
		for d in dictlist:
			writer = csv.DictWriter(csvfile, fieldnames = d.keys(), dialect = 'excel')
			# writer.writerow(['love','reviewers','hasTargetCity','street','blvd','ave','hasCity','hasTargetBusinessNameText','ratings','hasTargetBusinessNameDomain','container','menu','comfort','rd','resort','recommended','profile','map','good','city','read','great','collection','hasPhoneNumber','profile','forum','st','reviews','hasReviewProvider','miles','hasDirectoryProvider','order','road','reserve'])
			# writer.writeheader()
			data = {key:value for key,value in d.items() if key in d.keys()}
			writer.writerow(data)


if __name__ == '__main__':
	sys.exit(main())
