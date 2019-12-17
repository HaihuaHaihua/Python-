'''
BeautifulSoup4库的基本元素

BeautifulSoup的理解

标签的基本格式
 <p>..</p>:标签Tag
 <p class="title">...<p>
 p名称是成对出现的 class="title"这样的“键值对”构成了标签的属性

BeautifulSoup库的引用

form bs4 from BeautifulSoup 一般情况
只判断bs4库的变量 可以使用 import bs4

html lxml文档解析器
 html.parser ->bs4库
 lxml 和 xml 都是lxml解析器 安装lxml库
 html5lib  html解析器

 -------------------------
 基本元素：
 Tag 标签 基本信息组织单元 用<>和</>表示开头和结尾
 Name 标签名 <p>...</p> p为名字  <tag>.name可以获取标签名
 Attributes 标签属性  <tag>.attrs
 NavigableString 标签内非属性字符串 <>...</>中的字符串 <tag>.string
 Comment 标签内的注释部分
 --------------------------
'''

import requests
from bs4 import BeautifulSoup
url="https://python123.io/ws/demo.html"
try:
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    demo = r.text
    soup=BeautifulSoup(demo,"html.parser")
    tag=soup.a #soup.a返回第一个a标签

    print(tag.name) #返回a标签的名字
    print(tag.parent.name) #返回a标签父亲的名字
    print(tag.parent.parent.name)
    
    print(tag.attrs) #返回a标签的属性 一个字典类型
    print(tag.attrs['class']) #返回a标签的class属性
    print(tag.attrs['href']) #返回a标签的链接属性
    print(type(tag.attrs)) #查看标签a属性的类型 字典类型 tag无属性时返回空字典
    print(type(tag)) #查看标签的类型 tag类型

    print(soup.a.string) #a标签之间的字符串 <a>....</a>
    print(soup.p.string) #p标签是a的父标签
    print(type(soup.p.string)) #soup.p.string 类型为NavigableString（可以跨越多个标签输出字符串）

    newsoup=BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>","html.parser")
    print(newsoup.b.string) #.string时没有输出注释部分 !-- --! 注释需要另做考虑
    print(type(newsoup.p.string))
    print(newsoup.p.string)
    print(type(newsoup.p.string))
except:
    print("爬取失败")
    

