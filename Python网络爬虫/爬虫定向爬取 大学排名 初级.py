#http://www.fakjdfjlas.com/robots.txt
#用robots.txt后缀查看网页是否通过robots协议来限制爬虫 来验证可行性
'''
大学排名定向爬虫
1.从网络上获取大学排名网页内容
    构造 getHTMLText()
2.提取网页内容中的信息到合适的数据结构中
    构造 fillUnivList()
3.利用数据结构并输出结果
    构造 printUnivList()
'''
import requests
from bs4 import BeautifulSoup #import bs4中的BeautifulSoup类
import bs4 #直接引用bs4

#输入为获取的url信息 输出url内容
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "爬取失败"

#将html页面放到ulist列表中
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag): #检测tr是否bs4库的标签类型 过滤字符串类型的children  需要引用bs4 使用其中对标签类的定义
            tds =tr ('td') #查询tr中的td标签 将需要的td标签添加到tds列表中
            ulist.append([tds[0].string,tds[1].string,tds[2].string]) #向列表类型ulist中添加字段[1,2,3] 大学排名 大学名称 大学评分

#将ulist中的信息打印出来 num控制打印的个数
def printUnivList(ulist,num):
    '''
    ********
    当中文字符宽度不够时，采用英文字符填充，中英文字符打印的宽度不同 导致格式不整齐
    中文宽度问题 采用中文字符的空格填充
        采用中文字符的空格填充 chr(12288) [中文空格的utf8编码]
    '''
    tplt = "{0:^10}\t{1:{3}^10}\t{2:{3}^10}" #{1:{3}^20}中的{3}表示调用format中的第四个参数 即chr(12288)
    print(tplt.format("排名","学校名称","学校地区",chr(12288))) 
    #print("{:^10}{:^20}{:^20}".format("排名","学校名称","学校评分",)) #打印表头 format(''1'',''2'',"3") format函数中123对应调用对象对应的槽{}
    #打印num个学校信息
    for i in range (num):
            u=ulist[i]
            #print("{:^10}{:^6}{:^10}".format(u[0],u[1],u[2]))
            print(tplt.format(u[0],u[1],u[2],chr(12288)))
    '''
    format()
    1.位置对应 "{0},{1}".format("abc","bcd") => abc,bcd
    2.关键字对应  "{name},{age}".format(age="abc",name="bcd") => bcd,abc
    3.下标对应 p=['abc','bcd']  "{0[0]},{1[1]}".format(p) =>abc,bcd

    格式限定符
    1.填充与对齐
        ^ 居中 ; < 左对齐; > 右对齐 限定符后带宽度
        冒号 : 后面带填充的字符 只能是一个 且默认为空格
        "{0:^10}".format("abc") 10个宽度居中输出abc 填充空格
        "{0:*>20}".format("bcd") 20个宽度右对齐输出bcd 填充*
    2.精度与类型
        "{0:.2f}".format(321.131312) => 321.13 长度为2的精度 float类型 
    '''
def main():
    uinfo = [] #定义一个列表uinfo
    url = "http://www.zuihaodaxue.cn/shengyuanzhiliangpaiming2017.html#top"
    html = getHTMLText(url) #获取url的text 并用html记录
    fillUnivList(uinfo,html) #将html中记录的信息存放到uinfo列表中
    printUnivList(uinfo,20) #打印uinfo中的20所学校

if __name__=="__main__":
    main()
