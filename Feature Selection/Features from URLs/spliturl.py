#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys

def split_url(url):
	# request_protocol = r'^\w+:\/\/'
	# domain = r'^\w+(?=:\/\/)'
	protocol_domain = r'^\w+:\/\/?[\w+.]+(?=\/|:\d+)'
	slash = r'\/'
	dash = r'\-'
	undersocre = r'\_'
	dot = r'\.'
	question_mark = r'\?'
	equals_sign = r'\='
	plus = r'\+'
	space = r'\s'
	ampersand = r'\&'
	quotation = r'\"|\''
	comma = r'\,'
	colon = r'\:'
	pipe = r'\|'
	url_encoding = r'%\d{2}|%\d{1}[ABCDEF]|%[ABCDEF]\d{1}|%[ABCDEF]{2}'

	regex = protocol_domain
	rest = filter(None, re.split(regex, url))
	# print rest
	regex2 = slash+'|'+dash+'|'+undersocre+'|'+dot+'|'+question_mark+'|'+equals_sign+'|'+plus+'|'+ space+'|'+ampersand+'|'+quotation+'|'+comma+'|'+colon+'|'+pipe+'|'+url_encoding
	return filter(None, re.split(regex2, rest[0]))


def main():
	print split_url("https://www.facebook.com/WishboneWashingtonBlvd?rf=167151823347690")
	print split_url("http://portalsso.vansd.org/portal/page/portal/Building_Pages/COLUMBIA_RIVER_HIGH_SCHOOL")
	print split_url("http://clubzone.com/bell-center-montreal/")
	print split_url("Bass+Pro+Shops 2C+300+Cincinnati+Mills+Dr 2C+Cincinnati 2C+OH")
if __name__ == '__main__':
	sys.exit(main())
