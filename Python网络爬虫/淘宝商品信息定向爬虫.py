#淘宝商品信息定向爬虫
'''
1.提交商品搜索请求，循环获取页面
2.对于每个页面，提取商品名称和价格信息
3.将信息输出到屏幕上
'''
import requests
import re

#获取页面信息
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "failure!"
    
#解析所获取的页面
def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html) #用正则表达式匹配price
        tlt = re.findall(r'\"raw_title\"\:\".*?"',html) #用正则表达式匹配title
        #截取价格和名称
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("failure!")
        
#输出解析后的信息
def printGoodslist(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))
        
def main():
    goods = '书包' #定义关键词变量
    depth = 2 #搜索深度
    start_url = 'https://s.taobao.com/search?q=' + goods #爬取的对象
    infoList = [] #获取的所有结果
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)  #s标记每个页面的商品数量 s= 44 88
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue #继续下一个页面的解析
        printGoodslist(infoList) #打印结果

main()


    
