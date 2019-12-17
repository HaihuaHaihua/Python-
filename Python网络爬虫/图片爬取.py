#图片爬取
import requests
import os
url="http://pic1.win4000.com/wallpaper/d/58747f2edb1ec.jpg" #图片的url
root="C://Users/regul/Pictures/" #文件夹根目录
path=root + url.split('/')[-1] #文件路径为 root+url 的‘/’的最后一个部分
try:
    if not os.path.exists(root): #判断根目录是否存在
        os.mkdir(root)
    if not os.path.exists(path): #判断路径是否存在
        r=requests.get(url)
        with open(path,'wb') as f: #open()打开一个文件 定义为文件标识符 f
            f.write(r.content) #图片为二进制格式 用二进制格式保存图片 r.content返回二进制形式
            f.close()
            print("accomplishment")
    else:
        print("failed")
except:
    print("paqushibai")
