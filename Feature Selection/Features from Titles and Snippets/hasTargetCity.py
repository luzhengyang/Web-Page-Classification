'''
Search for a target city in title and snippet
'''

from geotext import GeoText

def has_target_city(target_city, text):
	TargetCity = {'hasTargetCity':0}
	places = GeoText(text)
	for city in places.cities:
		if target_city.upper() == city.upper():
			TargetCity['hasTargetCity'] = 1
			break
		else:
			pass

	return TargetCity