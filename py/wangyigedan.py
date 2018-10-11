#encoding = "utf-8"
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
	try:
		html=urlopen(url)
	except HTTPError as e:
		return None
	try:
		a = BeautifulSoup(html.read(),features='html.parser')
		# features='html.parser'有助于消除警告
		title = a.title
	except AttributeError as e:
		return None
	return title
f = open("a.txt","w")
title = getTitle("http://www.baidu.com")

if title == None:
	print("title is None",file = f)
else:
	print(title,file = f)
        
            
            
