from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.purepen.com/sgyy/")
a = BeautifulSoup(html,from_encoding="GBK",features='html.parser')
bsh=a.findAll("font",{"color":"#000000"})
for sa in bsh:
	msg=sa.tr.get_text()
	print(msg)
