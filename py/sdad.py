from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.baidu.com")
a = BeautifulSoup(html.read(),features="html.parser")
print(a.get_text())
