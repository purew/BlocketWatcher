 # -*- coding: iso-8859-15 -*-

import urllib
import re



def findAds():
	baseURL = "http://www.blocket.se/hela_sverige"
	options = "?q=marantz+ELLER+onkyo&cg=0&w=1&st=s&st=u&st=b&ca=15&md=th"
	website = urllib.urlopen(baseURL+options)

	#html = website.read()
	f = file("stereo.html", "r")
	html = f.read()
	
	regExp = '<td nowrap="nowrap" class="thumbs_subject">.*?<a href="(.*?)">\s*(.*?)\s*</a><br>\s*([\d| ]*)'
	m = re.findall(regExp,html, re.DOTALL)
	
	itemList = []
	for item in m:
		price = item[2]
		price = price.replace(' ','')
		itemList.append((item[1],price))
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
