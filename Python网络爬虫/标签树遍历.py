'''
基于bs4的HTML内容的遍历
 
1.标签树的下行遍历
    .contents 子节点的列表 ，将<tag>所有儿子的节点存入列表
    .children 子节点的迭代类型，与.contents类似，用于循环遍历儿子节点
    .descendants 子孙节点的迭代类型，包含所有子孙节点，用于循环遍历
2.标签树的上行遍历
    .parent 节点的父亲标签
    .parents 节点的先辈标签的迭代类型，用于循环遍历先辈节点
3.标签树的平行遍历
    .next_sibling 返回按照html文本顺序的下一个平行节点标签
    .previous_sibling 返回按照html文本顺序的上一个平行节点标签
    .next_siblings 迭代类型，返回按照html文本顺序的后续所有平行节点标签
    .previous_siblings 迭代类型，返回按照html文本顺序的前续所有平行节点标签
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
    #------下行遍历
    print(soup.head)
    print(soup.head.contents) #遍历head的子节点
    print(soup.body.contents) #遍历body的子节点 标签的子节点既包括标签节点 也包括 字符串节点
    print(len(soup.body.contents)) #用len() 的到body子节点个数
    print(soup.body.contents[1]) #打印body的第二个子节点 
    #------上行遍历
    print(soup.title.parent)
    print(soup.html.parent) #html的父标签是自己
    print(soup.parent) #soup的父标签没有.name
    #标签循环打印上行标签的name
    for parent in soup.a.parents:
        if parent is None:
            print(parent) #不存在先辈是不打印其名字
        else:
            print(parent.name)
    #------平行遍历 所有平行遍历发生在同一个父亲节点下的各节点间
    print(soup.a.next_sibling) #标签间的navigable string也构成标签树的节点 任何一个节点的 子标签 平行标签 不一定是标签类型 也可能是 navigab string 类型
    print(soup.a.next_sibling.next_sibling)
    print(soup.a.previous_sibling)
    print(soup.a.previous_sibling.previous_sibling)
    print(soup.a.parent)
    #平行循环遍历 _siblings 迭代类型用在 for foreach语句中 
    for sibling in soup.a.next_siblings:
        print(sibling)
    
    #print(demo)
    
except:
    print("爬取失败")
