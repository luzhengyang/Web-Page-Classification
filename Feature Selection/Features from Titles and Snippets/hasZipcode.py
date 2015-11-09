'''
Search for zip code in title and snippet
'''

import re

def has_zip_code(text):
	regex = r"(^\d{5}(-\d{4})?$)|(^[ABCEGHJKLMNPRSTVXY]{1}\d{1}[A-Z]{1} *\d{1}[A-Z]{1}\d{1}$)"

	ZipCode = {'hasZipCode':0}

	if re.findall(regex, text):
		ZipCode['hasZipCode'] = 1
	else:
		pass

	return ZipCode