#ip地址归属地自动查询
import requests
url = "http://m.ip138.com/ip.asp?ip=" #用IP138工具来查询IP地址归属地
try:
    r=requests.get(url + '202.204.80.112') #输入想要查询的IP地址 ip=
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")
