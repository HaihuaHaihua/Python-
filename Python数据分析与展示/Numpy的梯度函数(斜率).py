##Numpy的梯度函数
'''
梯度：连续值之间的变化路 即斜率 b=(c-a)/d   a , b , c顺序的三个坐标 d为 c与a的距离 
np.gradient(f)
'''
import numpy as np

a = np.random.randint(0,20,(5))
print(a)
print(np.gradient(a)) #计算a中每个元素位置的梯度 两侧值(c-a)/2 单侧值(b-a)/1

#二维数组梯度
b = np.random.randint(0,20,(3,5))
print(b)
print(np.gradient(b)) #生成两个b.shape的数组 分别表示元素在第一维度和第二维度的梯度
#n维数组的 np.gradient() 会生成原shape的n个数组 分别表示元素在每一个维度的不同梯度
