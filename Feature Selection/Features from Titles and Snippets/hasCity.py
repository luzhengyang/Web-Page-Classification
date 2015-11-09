'''
Search for a city in title and snippet
'''

from geotext import GeoText



def has_city(text):
	City = {'hasCity':0}

	places = GeoText(text)
	if places.cities != []:
		City['hasCity'] = 1
	else:
		pass
				
	return City



