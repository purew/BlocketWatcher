 # -*- coding: utf-8 -*-


import urllib
import re

def utf8(str):
	"""Translate a latin1-string to utf8-encoding."""
	
	return unicode(str, "iso-8859-1").encode("utf-8")



def findAds():
	"""Fetch ads from blocket and other ad-sites."""
	
	baseURL = "http://www.blocket.se/hela_sverige"
	options = "?q=marantz+ELLER+onkyo&cg=0&w=1&st=s&st=u&st=b&ca=15&md=th"
	website = urllib.urlopen(baseURL+options)

	CACHED_WEBSITE = False
	
	if not CACHED_WEBSITE:
		html = website.read()
	else:
		f = file("stereo.html", "r")
		html = f.read()
	
	regExp = '<td nowrap="nowrap" class="thumbs_subject">.*?<a href="(.*?)">\s*(.*?)\s*</a><br>\s*([\d| ]*)'
	m = re.findall(regExp,html, re.DOTALL)
	
	itemList = []
	for item in m:
		header = utf8(item[1])
		price = item[2]
		price = price.replace(' ','')
		itemList.append((header,price))
	return itemList
	
	

		
# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
	
	m = findAds()
	
	for item in m:
	#for i in range(len(m),0):
		print "**************************"
		#print item.group(1)
		print "Föremål: "+item[0]
		print item[1]
