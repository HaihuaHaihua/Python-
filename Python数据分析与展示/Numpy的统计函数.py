##Numpy的统计函数
'''
np的统计函数
    np.sum(a,axis=None)  根据给定轴axis计算数组的a的相关元素之和
    np.mean(a,axis=None) 根据给定轴axis计算数组的a的相关元素的期望
    np.average(a,axis=None,weights=None) 加权平均值
    np.std(a,axis=None) 标准差
    np.var(a,axis=None) 方差
    axis表示统计运算所处的维度

    np.max()/min() 最大值，最小值
    np.argmax()/argmin()  一维化后 最大值、最小值在数组中的位置
    np.unravel_index(index,shape) 根据shape将下标index转化为多维下标 可以和argmax()/argmin()联用
    np.ptp(a) 数组a中最大值和最小值的差
    np.median() 中位数
'''
import numpy as np

a = np.arange(15).reshape(3,5)
print(a)
print(np.sum(a))
print(np.mean(a,axis=1)) #axis=1将数组的第二维度的元素进行期望计算
print(np.mean(a,axis=0))
print(np.average(a,axis=0,weights=[10,5,1])) #weight 对第一维度的每个集合进行加权
print(np.std(a)) #标准差 
print(np.var(a)) #方差

b = np.arange(15,0,-1).reshape(3,5)
print(b)
print(np.max(b))
print(np.min(b))
print(np.argmin(b)) #一维化后 b中最小值的下标
print(np.unravel_index(np.argmin(b),b.shape)) #以argmin(b)为index 以b.shape为shape转化多维下标
print(np.ptp(b))
print(np.median(b))
