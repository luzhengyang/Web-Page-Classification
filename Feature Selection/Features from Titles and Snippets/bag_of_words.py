'''
Bag-of-words
'''

import nltk

def bag_of_words(text):
	# f = file(filename, 'rb')
	# content = f.read().decode('ascii','ignore')
	tokens = nltk.word_tokenize(text)

	word_dict = {'ave':0, 'rd':0, 'map':0, 'road':0, 'street':0, 'city':0, 'blvd':0, 
	'resort':0, 'st':0, 'profile':0, 'reviews':0, 'menu':0, 'read':0, 'great':0, 
	'order':0, 'reserve':0, 'comfort':0, 'good':0, 'love':0, 'recommended':0, 'reviewers':0, 
	'forum':0, 'miles':0, 'collection':0, 'container':0, 'ratings':0, 'search':0}

	words = ['ave', 'rd', 'map', 'road', 'street', 'city', 'blvd', 
	'resort', 'st', 'profile', 'reviews', 'menu', 'read', 'great', 
	'order', 'reserve', 'comfort', 'good', 'love', 'recommended', 'reviewers', 
	'forum', 'miles', 'collection', 'container', 'ratings', 'search']

	for key in word_dict:
		word_dict[key] = 0

	for word in words:
		for token in tokens:
			if token.upper() == word.upper():
			# if token.upper() == word.decode('utf8','ignore').upper():
				word_dict[word] += 1

	return word_dict

	# with open('BOW.csv','w') as csvfile:
	# 	writer = csv.DictWriter(csvfile,fieldnames = word_dict.keys())
	# 	writer.writeheader()
	# 	data = {key:value for key,value in word_dict.items() if key in word_dict.keys()}
	# 	writer.writerow(data)
