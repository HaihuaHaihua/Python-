#BeautifulSoup4使用 可以解析任何标签格式的文本  html sml文件
# BeautifulSoup4库是 解析 遍历 维护 “标签树”的功能库
# from bs4 import BeautifulSoup 从bs4中创建一个BeautifulSoupd对象
#soup= BeautifulSoup(<data>,html)
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
except:
    print("爬取失败")
