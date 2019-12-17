##Pandas数据特征
'''
数据排序 .sort_...
    .sort_index() 对索引排序
    .sort_values() 对元素值排序
    axis=n 修改排序轴 ascending=True/False 升序降序
    DataFrame.sort_values(by, axis= ,ascending= )  二维多了一个by参数 axis轴上的索引列表
'''
import pandas as pd
import numpy as np

##数据排序

#对索引排序 
d = pd.DataFrame(np.arange(20).reshape(4,5),index=['c','d','b','a'])
print(d)
c = d.sort_index(axis=1, ascending=False) #axis=0 行索引 Index / axis=1 列索引 columns
print(c)
c = c.sort_index() #默认 0轴 升序
print(c)
#对元素值排序
b = pd.DataFrame(np.random.randint(0,20,(4,5)),index=['c','d','b','a'])
b = b.sort_values(2, ascending=True)
print(b)
b= b.sort_values('a',axis=1, ascending=False)  #以第a行 降序排序
print(b)
a = pd.DataFrame(np.arange(12).reshape(3,4),index=['a','b','c'])
c = a + b
print(c.sort_values(2,ascending=True))  #数据排序中 NaN 默认排在末尾

##数据统计
#函数与numpy相同 .sum() .median() 等.... 默认按0轴计算 及 纵轴计算
#.describe() 得到数据的诸多特征 一次性输出
a = pd.Series(np.random.randint(1,20,4),index=['a','b','c','d'])
print(a.describe())
print(a.describe()['count']) #获得元素个数 利用的是describe()生成的Series对象的索引 count
print(d.describe()) #DataFrame获得的describe()仍是DataFrame类型 计算的是纵轴数据的信息
print(d.describe().ix['min']) #获得每一列的最大值 获得行数据 DataFrame.ix['索引']
print(d.describe()[2]) #获得第二列的数据信息

##数据累计统计分析
'''
.cumsum() 前n个数的和  .cumpord() 积 .cummax() 最大值 .cummin() 最小值
滚动计算 .rolling(w).sum()  计算相邻w个元素的和 .rolling(w).mean() 计算相邻w个元素的算术平均值.... 
'''
print(d.cumsum()) #计算当前位置元素与当前列之前元素的累加和
print(d.rolling(2).sum) #在纵向上以两个元素为单位求和
print(d.rolling(3).mean)

##数据相关性判断
'''
通过协方差判断 cov(X,Y)  >0 正相关 <0 负相关 =0不相关
Pearson相关系数r  r[-1,1]  0.8-1.0 极强相关 0.6-0.8强相关 0.2梯度递减 可以多加理解 
    .cov() 计算协方差矩阵 .corr() 计算相关系数 Pearson等一大堆系数
'''
hprice = pd.Series([3.04,22.93,12.75,22.6,12.33], index=['2008','2009','2010','2011','2012'])
m2 = pd.Series([8.18,18.38,9.13,7.82,6.69], index=['2008','2009','2010','2011','2012'])
print(hprice.corr(m2)) #计算 hprice 和 m2 的相关系数
               
