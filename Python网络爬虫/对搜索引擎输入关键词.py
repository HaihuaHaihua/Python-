#用requests库对搜索引擎提交关键词
#百度https://www.baidu.com/s?wd=keyword     wd
#360https://www.so.com/s?q=keword       q
import requests
keyword="Python"
try:
    kv={'wd':keyword}
    r=requests.get("https://www.baidu.com/",params=kv)
    print(r.request.url)#r.requests.url错误 request来调用
    r.raise_for_status()
    print(len(r.text))
    print(r.text)
except:
    print("爬取失败")
