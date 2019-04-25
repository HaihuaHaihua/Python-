## Numpy数据分析

### 条件查找数组元素

#### 一维数组查找满足条件元素

​	array[condition] : 直接在中括号中加条件，得到的即是满足条件新的一维数组

```python
import numpy as np
arr = np.arange(10)
print(arr)
arr2 = arr[arr % 2 == 1] #获得数组中所有的奇数
print(arr2)
#[1 3 5 7 9]
```

​	当然，既然可以索引到元素位置，也可以对指定位置的元素值，直接进行修改

```python
arr[arr % 2 == 1] = -1
print(arr)
#[0 -1 2 -1 4 -1 6 -1 8 -1]
```

​	对于多维数组则使用`where(condition,value,object)`方法实现指定条件元素替换

```python
arr3 = arr.reshape(2,5)
print(arr3)
out = np.where(arr3 % 2 == 1, -1, arr3)
print(out)
#[[0 -1 2 -1 4],[-1 6 -1 8 -1]]
```

​	使用where(condition)来获取符合条件的元素下标

```python
a = np.arange(10)
index = np.where((a>=3)&(a<=8)) #获取a数组中大于3小于8元素的下标
print(a[index])
# [3 4 5 6 7 8]
# 当然也可以直接设定条件获取数组指定元素
print(a[(a>=3)&(a<=8)])
```

#### 数组扩充

* 数组间垂直叠加(行扩展)

```python
import numpy as np
a = np.zeros((2,5))
b = np.ones((2,5))
print("a:\n",a)
print("b:\n",b)
#垂直叠加 vstack()
print("[a,b]:\n",np.vstack([a,b]))
print("[a,b]:\n",np.concatenate([a,b],axis=0))
```

* 数组间水平叠加(列扩展)

```python
#水平叠加 hstack()
print("[ab]:\n",np.hstack([a,b]))
print("[ab]:\n",np.concatenate([a,b],axis=1))
```

* 重复元素：repeat(array,reps) 针对数组元素的重复 ；tile(array,reps) 针对数组的重复

```python
import numpy as np
array = np.array([1,2])
print(np.repeat(array,[3,2]))
print(array.repeat([3,2]))
print(np.tile(array,[3,2])) #以数组为单位进行3X2的copy
#高维数组的操作
array = np.array([[1,1],[2,2]])
print(array)
arr1 = array.repeat([3,2],axis=0) #对最高维数组的元素重复
arr2 = array.repeat([3,2],axis=1) #以数组为单位重复
arr3 = np.tile(array,[3,2])
```

#### 数组特征值

​	计算数组的均值、中位数、标准差：mean() median() std()

```python
import numpy as np
array = np.arange(10)
mu,med,sd = np.mean(array),np.median(array),np.std(array)
print(mu,med,sd)
array2 = array.reshape((2,5))
print(array2.mean(),array2.median(),array2.std())
```



