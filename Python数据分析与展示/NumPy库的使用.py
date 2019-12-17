
###NumPy库的使用
'''
    numpy库科学计算基础库
    1.强大的N维数组对象 ndarray
    2.广播功能函数
    3.整合C/C++/Fortran 代码的工具
    4.线性代数、傅里叶变换、随机数生成等功能

    N维数组对象：ndarray
    1.将一维数组向量看做一个单个数据 进行计算 省去了数组中单个元素间运算所需要的循环
    2.用数组对象优化可以提升运算速度

    ndarray的组成（数组所有的元素类型相同 数组下标从0开始）
    1.实际数据
    2.数据的描述（数据类型，数据维度等）

    生产一个ndarray数组: np.array()
    ndarray的 1.轴（axis）：保存数据的维度  2.秩（rank）：轴的数量

    ndarray对象的属性：
    1. ndim  对象的秩
    2. shape  对象的尺度 对于矩阵就是 n行m列
    3. size     对象元素的个数  对于矩阵就是 n*m个
    4. dtype  对象元素的数据类型
    5. itemsize  对象的元素大小 byte

    ndarray的元素支持多种数据类型 
'''
###ndarray数组的创建与变换
'''
 ndarray数组创建
     1.从Python中的列表（list）、元组（tuple）等类型创建
         x = np.array()list/tuple)
         x = np.array(list/tuple,dtype = np.float32)  #dtype来确定元素的数据类型
         当创建时不指定dtype时，dtype与数据状况匹配
    2.（常用方法）使用Numpy中的函数创建
        arange(n)  返回ndarray类型，生成从0到n-1为元素的数组(arange元素为整数类型 下面4种方法为浮点类型)
        ones(shape)  生成shape维度的 全1数组 shape为元组类型
        zeros(shape)  生成全0数组
        full(shape,val) 生产 一个shape维度的 全元素为val的 数组
        eye(n)  创建一个n*n的矩阵 对角线为1 其余全为0

        ones_like(a)  zeros_like(a)   full_like(a,value) 生成a数组shape的对应全同元素数组

        linspace(s, e ,sp ,endpoint=false/true ) 根据起止数据等间距的填充数据 （插入数据）
            第一个参数s 起始元素的值 第二个参数e 结束元素的值 第三个参数总共生成元素的个数
            在s和e之间等值差距填充  相邻元素差值为(e-s)/(sp-1)   第四个参数endpoint是否生成结束元素 不生成e时 相邻元素差值(e-s)/sp
            
        concatenate( (a,b),(c,d,e) .... ) 将两个或者多个数组合并成一个新的数组

ndarray数组的变换
    维度变换
        reshape(shape) 保证不改变数组元素 返回shape形状数组 不改变原数组
        resize(shape)  与reshape()相同  修改原数组
        swapaxes(ax1,ax2) 将数组n个维度中两个维度进行调换
        flatten() 对数组进行降维 变成一个一维数组 数组总元素不变 不改变原数组
    类型变换
        .astype(new_type) 创建了一个新数组
    数组向列表转换
        list=a.tolist()
'''

##计算 C = A2 + B3
'''
def pySum():
    a = [0,1,2,3,4]
    b = [9,8,7,6,5]
    c = [ ]
    
    for i in range(len(a)):
        #c[i] = a[i]**2 + b[i]**3
        c.append(a[i]**2 + b[i]**3)
        #list.append() 方法用于在列表末尾添加新对象
    return c

print(pySum())

'''
import numpy as np

def npSum():
    a = np.array([0,1,2,3,4])
    b = np.array([9,8,7,6,5])
    c = a**2 + b**3
    return c

print(npSum())

n = np.array([ [0,1,2,3,4],
                         [9,8,7,6,5] ])
print(n.ndim)
print(n.shape)
print(n.size)
print(n.dtype)
print(n.itemsize)

print( "第一种方法创建ndarray")
x1 = np.array([1,2,3,4]) #列表创建
y1 = np.array((5,6,7,8)) #元组创建
z1 = np.array([[1,2],[3,4],(5,6,7,8)]) #列表加元组(类型相同时)创建
print(x1)
print(y1)
print(z1)

print("第二种方法创建ndarray")
print(np.arange(10))
print(np.ones((3,6)))
print(np.zeros((3,6)))
print(np.full((3,6,4),6))
print(np.eye(6))

a = np.linspace(1,10,4)
print(a)
b = np.linspace(1,10,4,endpoint=False)
print(b)
c = np.concatenate((a,b))
print(c)

print("ndarray数组的维度变换")
a = np.ones((2,3,4),dtype=np.int32)  #类型np.size
print(a)
print(a.reshape((3,8)))
print(a.reshape((2,2,2,3))) #2*3*4=3*8=2*2*2*3=24保证元素个数不变
print(a) #reshape不改变原数组
print(a.resize((3,8)))
print(a) #resize改变原数组
b = a.flatten()
print(b)
print(a) #flatten() 降维 不改变原数组

print("ndarray数组的类型变换")
print(a.astype(np.float))
c = a.astype(np.float)
print(c)

print("ndarray数组向列表转换")
print(a.tolist())
