#! /usr/bin/python3.8

import os
import requests
import bs4

term = input('Enter a term to search: ')
url = f'https://www.istockphoto.com/br/en/photos/{term}?phrase={term}&sort=mostpopular'

re = requests.get(url)
re.raise_for_status()
soup = bs4.BeautifulSoup(re.text, "html.parser")
img_tags = soup.find_all(class_='gallery-asset__thumb gallery-mosaic-asset__thumb')
print(f'Total images: {len(img_tags)}')
print(f'Creating a directore named {term}.')
os.mkdir(term)
os.chdir(term)
print('Done')
for img_tag in img_tags:
    url_img = img_tag['src'].split('?')[0]
    print(f'Dowloading {url_img}...')
    re_img = requests.get(url_img)
    re.raise_for_status()
    img_file_name = url_img.split('/')[-1] + '.jpg'
    print(f'Saving {img_file_name}...')
    with open(img_file_name, 'wb') as img_file:
        for chunk in re_img.iter_content(10000):
            img_file.write(chunk)
