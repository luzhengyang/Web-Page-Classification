'''
Search for phone number in title and snippet
'''

import re

def has_phone_number(text):
	# filename = "/Users/zhengyanglu/Desktop/Classification/Profile/Title_Snippet/1-800-Got-junk?/bing_3.txt"
	# f = file(filename, 'rb')
	# content = f.read().decode('ascii', 'ignore')

	regex = r"\D*([2-9]\d{2})(\D*)([2-9]\d{2})(\D*)(\d{4})\D*"

	PhoneNumber = {'hasPhoneNumber':0}
	# for key in PhoneNumber:
	# 	PhoneNumber[key] = False

	if re.findall(regex, text):
		PhoneNumber['hasPhoneNumber'] = 1
	else:
		pass

	return PhoneNumber