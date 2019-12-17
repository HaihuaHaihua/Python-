#爬取网页的通用代码框架
import requests

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30) #请求url链接
        r.rasie_for_status() #根据response对象判断返回内容是否正常 如果状态码不是200则异常
        r.encoding=r.apparent_encoding #内容解码正确
        return r.text #返回内容
    except:
        return "产生异常"

if __name__=="__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))
