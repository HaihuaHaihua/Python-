## Numpy基础篇

​	用来进行多维数组的科学计算

### Numpy创建数组

* array()：一个普通数组

```python
import numpy as np
array = np.array([1,2,3])
print(array)
for i in range(3):
    print(array[i])
for i in array:
    print(i)
```

* zeros(shape) : 全零数组 ；ones(shape) : 全1数组 ；random.random(shape) : 全随机数数组

```python
import  numpy as np
zero = np.zeros((3))
one = np.ones((3))
random = np.random.random((3))
print(zero,one,random)
```

* arange(n) : 创建[0,n)间的等差数列

```python
import numpy as np
array = np.arange(10)
print(array)
#利用reshape(shape)方法创建多维数组
array1 = np.arange(10).reshape(2,5)
array2 = np.arange(27).reshape(3,3,3)
print(array1)
print(array2)
```

* full(shape,value) : 创建全为value的shape维度数组

```python
import numpy as np
array = np.full((3,3),4)
print(array)
```

* full((shape), True , dtype = bool) : 创建shape的布尔数组

```python
import numpy as np
array = np.full((3,3),True,dtype = bool)
print(array)
#使用用ones()方法实现
array2 = np.ones((3,3),dtype = bool)
print(array2)
```

* eye() : 创建n维`E`矩阵，对角线为1 

```python
import numpy as np
array = np.eye(3,3)
print(array)
```

* linspace(start,end,number) : 创建[start,end)个数为number等间距一维向量

```python
import numpy as np
array = np.linspace(0,10,3)
print(array)
```



### Numpy数组操作

1. 切片

   * 使用元素行列值获取元素
   * 使用`：`批量获取元素
   * 多维数组中使用`:`进行切片

   ```python
   import numpy as np
   array = np.array([[11,12],[21,22]])
   a21 = array[2][1]
   a1 = array[:,1]
   print(a21)
   print(a1)
   
   a = np.array([[11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20],
                 [21, 22, 23, 24, 25],
                 [26, 27, 28 ,29, 30],
                 [31, 32, 33, 34, 35]])
   print(a[0, 1:4]) # >>>[12 13 14]
   print(a[1:4, 0]) # >>>[16 21 26]
   print(a[::2,::2]) # >>>[[11 13 15]
                     #     [21 23 25]
                     #     [31 33 35]]
   print(a[:, 1]) # >>>[12 17 22 27 32]
   ```

   ![pic numpyClip](D:\Blog\PythonReview\Numpy\numpyClip.png)

2. 运算

   * 元素运算
   * 矩阵运算

   ```python
   import numpy as np
   a = np.array([[1,2],[3,4]])
   b = np.array([[5,6],[7,8]])
   Sum = a + b
   Dif = a - b
   Mul = a * b
   Div = a / b
   #矩阵乘法
   MulMat = a.dot(b)
   print(Sum)
   print(Dif)
   print(Mul)
   print(Div)
   print(MulMat)
   ```

   * transpose() : 矩阵转置

   ```python
   import numpy as np
   a = np.array([1,2,3])
   b = np.transpose(a)
   print(a)
   print(b)
   ```

[参考NumPy中文文档](<https://www.numpy.org.cn/article/basics/index.html>)





