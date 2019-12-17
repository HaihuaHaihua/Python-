##Numpy中的一些函数
'''
numpy的随机数函数 random子库 为数组类型提供生成随机数组的功能

生成随机数组
    np.random.rand() 在[0,1)之间随机产生浮点数
    np.random.randn() 标准正态分布中的数
    np.random.randint(low,high,(shape)) 在[low,high)之间产生随机整数或数组
    np.random.seed(s) 随着数种子 s是给定的种子值 使用相同的种子值可以得到相同的随机数
特殊的随机排序
    np.random.shuffle(a)  对数组的第1轴(第一维的首元素)进行随机排列，改变原数组
    np.random.permutation(a) 对数组a的第1轴产生一个新的乱想数组，不改变原数组
    np.random.choice(a,(size),replace=false,p) 从一维数组a中以概率p抽取元素，形成size形状的新数组，replace表示数组是否可以重用元素，默认false
带有分布的函数
    low起始值，high结束值，size形状，loc均值，scale标准差，lam随机事件发生率
   np.random.uniform(low,high,size) 具有均匀分布的数组
   np.random.normal(loc,scale,size)  正态分布的数组
   np.random.poisson(lam,size) 具有泊松分布的数组
    
'''
import numpy as np

a = np.random.rand(3,4,5)
print(a)
b = np.random.randn(3,4,5)
print(b)
c = np.random.randint(100,200,(3,4))
print(c)

#随机数种子
np.random.seed(8)
print(np.random.randint(100,200,(3,4)))
print(np.random.randint(100,200,(3,4)))
np.random.seed(8) #采用相同的种子值 生产相同的随机数组
print(np.random.randint(100,200,(3,4)))

print("高级随机操作")
print(np.random.permutation(c)) #不改变原数组
print(c)
print(np.random.shuffle(c))#改变原数组
print(c)
#choice()
b = np.random.randint(100,200,(8))
print(b)
print(np.random.choice(b,(3,2)))
print(np.random.choice(b,(3,2),replace=False)) #不可重用
print(np.random.choice(b,(3,2),p = b/np.sum(b))) #p的设定 元素数值越大被抽取的概率越大

##具有分布的数组
u = np.random.uniform(0,10,(3,4)) #均值分布
print(u)
n = np.random.normal(10,5,(3,4)) #正态分布
print(n)
p = np.random.poisson(5,(3,4)) #泊松分布
print(p)
