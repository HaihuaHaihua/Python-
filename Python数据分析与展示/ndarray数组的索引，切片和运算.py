##ndarray数组的索引和切片
'''
索引：获取数组中特定位置的元素
切片：获取数组中元素子集
'''
import numpy as np #numpy重命名为np
print("一维数组的索引和切片")
a = np.array([9,8,7,6,5])
print(a[2]) #索引
#起始下标 ：终止下标（小于 不包括终止下标对应的数值） ：步长
print(a[1 : 4 : 2]) # 1 ：4 表示第 1,2,3三个元素 步长为2 下标间隔为2  下标从0开始

print("多维数组的索引")
b = np.arange(24).reshape((2,3,4))
print(b)
print(b[1,2,3]) #每个维度上指定序号
print(b[-1,-2,-3]) #负号是从右到左 

print("多维数组的切片")
#在每一个维度上都使用冒号的方法   a ：b ：c
print(b[: , 1 , -3]) # 冒号选择整个第一个维度 
print(b[:, 1:3 , :]) #每个维度的切片与一维相同
print(b[:, :, : : 2]) #第三维度的两个冒号 使用步长进行跳跃切片 每个维度可以使用步长进行跳跃切片

##ndarray数组的运算
'''
数组与标量之间的运算 == 数组中的每一个元素都与标量进行运算
    一元函数 单目
        np.abs() / np.fabs() 计算数组各元素的绝对值
        np.sqrt() 计算平方根
        np.square() 计算平方
        等等......一堆函数
    二元函数 双目
         + - * /  **
         np.maximun(x,y) /np.fmin(x,y) 取元素级 最大最小值
          < > = !=  <= >= == 逻辑判断 产生bool类型原shape数组
'''
print("数组与标量之间的运算")
print(b.mean()) #a.mean()表示数组中所有元素的算术平均值
print(b/b.mean()) #数组与标量进行运算

print("numpy一元函数例子")
print(np.square(b)) #新生成新的数组 不改变原数组
print(np.sqrt(b))
print(np.modf(b)) #生成两个新的数组 第一个数组放小数部分 第二个数组放整数部分

print("numpy二元函数例子")
c = np.sqrt(b)
print(c)
print(np.fmax(b,c))
print(c<b)
