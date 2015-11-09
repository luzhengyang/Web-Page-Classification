'''
Search for a business name in title and snippet
'''

def has_business_name_in_text(businessName, text):

	BusinessName = {'hasBusinessName':0}

	for name in business_name_list:
		if name.upper() in text.upper():
			BusinessName['hasBusinessName'] = 1
			break
		else:
			pass

	return BusinessName

# filename = "/Users/zhengyanglu/Desktop/Classification/Profile/Title_Snippet/1-800-Got-Junk?/bing_6.txt"
