'''
信息标记形式
    XML 格式几乎与html相同
        1.有内容： <name>..内容..</name>
        2.无内容： <name /n> 省去一对尖括号
        3.注释：    <！   > 尖括号加感叹号
        扩展性好 但是书写繁琐
        XML 用于internet上的信息交互和传递
        
    JSON 有类型的键值对 "key":"value"
        键值对的 键 值 均有数据类型 当为字符串时 要用双引号
        "name":["hello","hi"]
        有类型的键 值 将信息组合
        1. "key":"value"
        2. "key":["value1","value2"]
        3. "key":{"subkey":"subvalue"} 键值对嵌套{  ，，} 就像标签下的标签
        适合程序处理 能作为程序的一部分 来源于JavaScript
        JSON用于移动应用云端和节点的信息通信中 用在程序对接口处理的地方 但无法注释
        
    YAML 无类型的键值对 key:value
        层次关系通过缩进的方式表示 所属关系
        用减号 - 表示并列关系
        用竖线 | 表示整块数据
        用井号 # 表示注释
        1.  key:value
        2.  key:#Comment
             -value1
             -value2
        3. key:
                subkey:subvalue
        文本信息比例最高 可读性好
        YAML用于各类系统的配置文件中
'''
'''
信息提取
 <>.find_all(name,attrs,recursive,string,**kwargs)
 find_all()方法 可以直接用 <tag>()或者soup() 来代替<>.find_all()
     name:对标签名称的检索字符串
     attrs:对标签属性值得检索字符串，可标注属性检索
     recursive:是否对子孙全部检索 默认True
     string:<>....</>中字符串区域的检索字符串 内容检索
 除了find_all 还有其他7中find方法
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
    #
    for link in soup.find_all('a'):
        print(link.get('href'))

    #----检索name参数
    print(soup.find_all('a'))#检索a标签
    print(soup(['a','b'])) #soup()==soup.find_all()
    #True时提取soup的所有标签信息
    for tag in soup.find_all(True):
        print(tag.name)

    #----检索attrs属性参数
    print(soup.find_all('p','course'))
    print(soup(id='link1')) #直接根据属性值约定来检索标签

    #----检索recursive参数
    print(soup.find_all('a'))
    print(soup('a',recursive=False))

    #----检索string参数
    print(soup.find_all(string="Basic Python"))#这种string提取需要准确输入才能提取出来 用正则表达式可以避免这种问题
    
except:
    print("爬取失败")
