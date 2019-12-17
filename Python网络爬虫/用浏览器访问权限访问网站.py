import requests
url="https://www.baidu.com/"
try:
    kv={'user-agent':'Mozilla/5.0'} #用Mozilla5.0浏览器作为访问名
    r=requests.get(url,headers=kv) #这里get不仅要使用url链接 还要用到header字段作为访问名
    r=requests.get(url)
    r.raise_for_status() #返回状态码 r.status_code
    #r.status_code
    r.encoding=r.apparent_encoding #解释返回内容为可读
    print(r.text[1000:2000]) #打印返回内容的1000到2000的字符
except:
    print("爬取失败") #检测后错误 try except
