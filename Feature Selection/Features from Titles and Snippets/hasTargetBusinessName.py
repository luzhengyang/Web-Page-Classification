# -*- coding: utf-8 -*-
'''
Search for a target business name in title and snippet
'''

import nltk
from nltk.corpus import stopwords
import string

def get_tokens(text):
	lowers = text.lower()
	no_punctuation = lowers.translate({ord(k): None for k in string.punctuation})
	tokens = nltk.word_tokenize(no_punctuation)
	return tokens

def has_target_business_name_in_text(target_business_name, text):
	TargetBusinessName = {'hasTargetBusinessNameText':0}
	tokenized_business_names = get_tokens(target_business_name)
	tokens = get_tokens(text)
	filtered = [w for w in tokens if not w in stopwords.words('english') and not w.isdigit()]
	for business_name in tokenized_business_names:
		for word in filtered:
			if business_name.upper() == word.upper():
				TargetBusinessName['hasTargetBusinessNameText'] = 1
				break
			else:
				pass

	return TargetBusinessName


def has_target_business_name_in_domain(target_business_name, domain):
	TargetBusinessName = {'hasTargetBusinessNameDomain':0}
	tokenized_business_names = get_tokens(target_business_name)
	for business_name in tokenized_business_names:
		if business_name.upper() in domain.upper():
			TargetBusinessName['hasTargetBusinessNameDomain'] = 1
			break
		else:
			pass

	return TargetBusinessName