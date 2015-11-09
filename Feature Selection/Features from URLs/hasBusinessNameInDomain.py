# from urlparse import urlparse
# import json

# page = json.load(file("/Users/zhengyanglu/Desktop/Classification/training-set-10-locations-2600-pages/bing/1-800-Got-Junk?/resultItemsMeta.json"))
# url_list=[]
# for key in page.keys():
# 	if key != "resultItemCount":
# 		# print page[key]["item"]["url"].decode('utf8','ignore')
# 		url_list.append(page[key]["item"]["url"].encode('utf8'))

# # Extract domain from URL in json file

# domain=[]
# for url in url_list:
# 	o = urlparse(url)
# 	domain.append(o.netloc)


# # Extract rest from URL in json file

# rest=[]
# for url in url_list:
# 	o = urlparse(url)
# 	rest.append(o.path)

def has_business_name_in_domain(businessName, domain):
	BusinessName = {'businessNameInURl':0}

	for name in business_name_list:
		if domain.upper().find(name.upper()) != -1:
			BusinessName['businessNameInURl'] = 1
			break
		else:
			pass

	return BusinessName


