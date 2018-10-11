from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen('http://www.baidu.com')   		  #打开url，获取html内容
bs_obj = BeautifulSoup(html.read(), 'html.parser')#把html的内容都传到BeautifulSoup对象
text_list = bs_obj.find_all("a", "mnav")       	  #找到“mnav”标签
for text in text_list:
	print(text.get_text())						  #循环打印
html.close()