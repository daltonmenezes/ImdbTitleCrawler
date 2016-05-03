from lxml import html
import requests

page = requests.get('http://www.imdb.com/title/tt0944947/')
tree = html.fromstring(page.content)
title = tree.xpath('//h1[@itemprop="name"]/text()')[0]

print title
