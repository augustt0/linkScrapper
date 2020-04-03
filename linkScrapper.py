from bs4 import BeautifulSoup
import urllib2
import re

# AUGUSTO CABRERA BIGEAGLE 2020
# https://github.com/augustt0/linkScrapper

def getLinks(link):
	html_page = urllib2.urlopen(link)
	soup = BeautifulSoup(html_page, features="lxml")
	links = []

	for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
	    links.append(link.get('href'))
	return links

# AUGUSTO CABRERA BIGEAGLE 2020
# https://github.com/augustt0/linkScrapper