#! /usr/bin/python3.8
# -*- coding: utf-8 -*-

import requests, pyperclip

url = 'https://baconipsum.com/api/'
n = input('Enter the number of paragraphs: ')
p = {
	'type': 'meat-and-filler',
	'paras': n,
	'format': 'json'
}
r = requests.get(url, params=p)
pyperclip.copy('\n'.join(r.json()))
print('Text copied into clipboard.')
