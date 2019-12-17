'''
基于bs4的html格式化和编码
用 .prettify() 可以将html按内容格式清晰打印出来
bs4将所有读入的内容都转化为utf8编码
'''
import requests
from bs4 import BeautifulSoup
url="https://python123.io/ws/demo.html"
try:
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    demo = r.text
    soup=BeautifulSoup(demo,"html.parser") #"html.parser" 是html的parser解释器
    #soup =BeautifulSoup('变量',"解释器")
    print(demo)
    soup.prettify() #prettify() 将每一内容后都加入了\n
    print(soup.prettify())
except:
    print("爬取失败")
