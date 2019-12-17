##numpy数据存取
'''
CSV存储批量数据

一维、二维数据存取
    np.savetxt(frame,array,fmt='%.18e',delimiter=None)  写入CSV文件
    np.loadtxt(frame,dtype=np.float,delimiter=None,unpack=False) 读取CSV文件
        frame 文件名 fmt/dtype数据类型 delimiter分隔符 unpack是否读入一个数组
任意维度数据存取
    (tofile fromfile 适合不同类型文件的对接)
    a.tofile(frame,sep='',format='%s') 文件写入
    np.fromfile(frame,dtype=float,count=-1,sep='') 文件读取
        从文件中读取元素是必须指定读取的数据类型 dtype
        count 读入元素的个数，-1表示读入整个文件
        sep 数据分隔符 空串 写入二进制文件
    a.tofile()和np.fromfile()需要配合使用 且读取的时候需要清楚源文件的维度和数据类型
numpy的便捷文件存取(程序中间进行文件缓存 这个方法很适用)
    np.save(fname,array) / np.savez(fname,array) 文件名 数组名 存储的文件必须使用 .npy的自定义扩展名
    np.load(fname) 必须读取默认格式文件 .npy或者 压缩.npz
'''
import numpy as np
import csv

##写入文件
a = np.arange(100).reshape(5,20)
np.savetxt('a.csv',a,fmt='%d',delimiter=',')
np.savetxt('a2.csv',a,fmt='%.1f',delimiter=',')

##打开CSV文件 import csv 然后用 csv_reader把每一行数据转化成一个list，每个元素均为字符串
csv_reader = csv.reader(open('a.csv',encoding = 'utf-8'))
for row in csv_reader :
    print(row)
csv_reader = csv.reader(open('a2.csv',encoding = 'utf-8'))
for row in csv_reader :
    print(row)

##读入文件
b = np.loadtxt('a.csv',delimiter = ',')
print(b)

##多维数组文件写入
c = np.arange(100).reshape(5,10,2)
c.tofile("d.dat",sep=",",format='%d')
c.tofile("e.dat",format='%d') #不指定分隔符变量 sep 这时生成的是占用存储空间更小的二进制文件

##任意维度文件读取
d = np.fromfile("d.dat",dtype=np.int,sep=',')
print(d)
d1 = np.fromfile("d.dat",dtype=np.int,sep=',').reshape(5,10,2)
print(d1)
#二进制文件读取
e = np.fromfile("e.dat",dtype=np.int).reshape(5,10,2)
print(e)

#便捷存取 save load
f = np.arange(100).reshape(5,5,4)
np.save("f.npy",f)
f2 = np.load("f.npy")
print(f2)
