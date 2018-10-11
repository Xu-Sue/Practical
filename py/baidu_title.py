from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://zhidao.baidu.com/question/9570293.html")
a = BeautifulSoup(html.read(),features="html.parser")
print(a)
