##Pandas库入门
'''
Pandas : 提供便于操作的数据类型和诸多分析函数和分析工具
    import pandas as pd 基于Numpy实现 常和Numpy和Matplotlib 联用

Series一维数据类型 带标签的数组 (索引+数据)
    Series类型可以由多种形式创建
    Series由 index索引属性 和 values值属性  .index  .values
    Series对象和索引都可以有名字 名字属性.name 索引名字属性 .index.name
    Series对象可以随时修改 
DataFrame 多维数据类型 (索引 + 数据1 + 数据2 + 数据3 .......)
    索引 纵向为index 索引轴为axis=0 横向索引为column
    行索引index 列索引column
(区分大小写)

Pandas数据类型操作
  重新索引 .reindex()改变或者重排Series和DataFrame索引
'''

import pandas as pd
import numpy as np

d = pd.Series(range(20))
print(d)
Sum = d.cumsum() #计算d中前i项和
print(Sum)

##Series类型

#从Python列表中创建Series
b = pd.Series([8,3,5,6], index=['a','b','c','d'])
b1 = pd.Series([8,3,5,6],['a','b','c','d']) #索引也可以作为第二参数直接放到Series()中 省去index=
print(b)
print(b1)
#从标量值创建Series
s = pd.Series(25,index=['a','b','c','d']) #标量25代表值 不能省略index=
print(s)
#从字典类型创建Series
e = pd.Series({'a':9, 'b':8, 'c':7}) #字典本身就具有键值对 含有索引 直接创建
f = pd.Series({'a':9, 'b':8, 'c':7}, index=['b','c','d']) #由index指定Series的结构，在字典中选取相关值
print(e)
print(f)
#从ndarray类型中创建Series
n = pd.Series(np.random.randint(1,100,5))
n1 = pd.Series(np.random.randint(1,100,5),index=np.random.randint(1,100,5))
print(n)
print(n1)

##Series基本操作  Series切片、运算等操作过后仍为Series类型
print(b.index)
print(b.values)
print(b['d'],b[3])  #系统生成索引0-n和自定义索引并存
print(b[['c','b','a',0]])  #两套索引不能同时使用
print(b[:3],b[:'d']) #提取0-3的元素 不包括3 但是用自定义索引 可以包含
print(b[b > b.median()]) # 提取大于中位数的元素
print(np.exp(b))
print('c' in b) #用in 判断索引是否在Series内 系统生成的索引无法判断
print(b.get('f',100)) #.get()方法 查找Series中是否有第一个参数 没有则返回第二个参数
print(b+e) #索引自动对齐(并集) 值为索引共同存在的值相加(交集)

b.name = 'Series b对象'
b.index.name = 'b索引列'
print(b)

##DataFrame类型

#从二维ndarray对象创建
d = pd.DataFrame(np.arange(10).reshape(2,5))
print(d)
#从一维ndarray对象字典创建
#遵守 行列索引自动补齐
dt = {'one':pd.Series([1,2,3],index=['a','b','c']),
           'two':pd.Series([9,8,7,6],index=['a','b','c','d'])}
d = pd.DataFrame(dt)
print(d)
d2 = pd.DataFrame(dt,index=['b','c','d'],columns=['two','three'])
print(d2)
#DataFrame操作
dl = {'城市': ['北京','上海','广州','深圳','沈阳'],
          '环比': np.random.randint(100,200,5),
          '同比': np.random.randint(100,200,5),
          '定基': np.random.randint(100,200,5),}
d3 = pd.DataFrame(dl,index=['a','b','c','d','e'])
print(d3)
print(d3['城市']) #获取列元素
print(d3.ix['b']) #获取行元素 .ix['']
print(d3['同比']['b']) #获取任意元素

##类型操作
#重排索引
d3 = d3.reindex(index=['e','d','c','b','a']) #index索引重排
print(d3)
d3 = d3.reindex(columns=['城市','同比','环比','定基']) #columns索引重排
print(d3)
newc = d3.columns.insert(4,'新增') #添加columns索引
newd = d3.reindex(columns = newc, fill_value=200) #用fill_value 为新增columns添加各行数值
print(newd)

#索引类型 
print(newd.index)
print(newd.columns) #Series和DataFrame 行列索引均为index 类型
'''
索引操作
.append(idx) 连接索引 产生一个新的索引
.diff() 差集 产生新的index对象
.intersection() 交集
.union() 并集
.delete() 删除对应位置的索引元素
.insert() 在对应位置增加索引元素
'''
dc = d3.columns.delete(2) #删除第2列
di = d3.index.insert(5,'f') #在第5行增加index 'f'
d4 = d3.reindex(index=di, columns=dc, fill_value=200) #method='ffill' 向前填充新数值 bfill 向后填充
print(d4)
#使用.drop()删除指定行列索引
d3 = d3.drop('a')
d3=  d3.drop('同比', axis=1) #删除 1轴上的元素 drop 默认对第0轴进行操作 可以用axis=n更改操作轴
print(d3)

##Series和DataFrame数据类型运算
x = pd.Series(np.arange(4))
y = pd.DataFrame(np.arange(20).reshape(4,5))
z = pd.DataFrame(np.arange(12).reshape(3,4))
print(z+y)
print(y.add(z, fill_value = 100)) #不同维度之间 不能用fill_value 或者说应该是不存在补齐操作
print(z.mul(y, fill_value = 0)) #用方法运算相对于 符号运算 可以提供参数修改 用fill_value参数替代默认补齐的NaN 再进行运算
#不同维度间的广播运算
print(x - 10)
print(y - x) # 默认在第1轴上运算
print(y.sub(x, axis=0)) #用axis参数设置 在第0轴上运算
#比较运算
s = pd.DataFrame(np.arange(20,0,-1).reshape(4,5))#比较运算 同维度比较需要尺寸相同
print(y>s) #比较运算 每个位置对应元素进行比较 生成一个bool类型 Pandas数据类型
print(y == x) #不同维度 默认在第一轴运算

