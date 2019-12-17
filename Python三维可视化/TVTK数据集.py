##TVTK数据集
'''
ImageData(spacing, origin , dimensions)
    spacing 起点坐标 origin 各坐标轴方法的间距 dimensions 各坐标轴上的网格数
    表示为二维或三维图像的数据结构（二维或三维数组）
RectilinearGrid
    间距不均匀的网格，所有点都在正交的网格上
StructuredGrid()
    可以创建任意形状的网格，需要制定点的坐标
Polydata
    由一系列的点之间的联系和点构成的多边形组成
'''

from tvtk.api import tvtk
import numpy as np

#ImageData数据集
img = tvtk.ImageData(spacing=(1,1,1),origin=(1,2,3),dimensions=(3,4,5))
print(img.get_point(0)) #第一个点的坐标
#获取前6个点的坐标
for n in range(6):
    print("%.1f,%.1f,%.1f"%img.get_point(n))

#RectilinearGrid数据集

#创建RectilinearGrid对象
x = np.array([0, 3, 9, 15])
y = np.array([0, 1, 5])
z = np.array([0, 2, 3])
r = tvtk.RectilinearGrid()
#r对象的属性设置
r.x_coordinates = x
r.y_coordinates = y
r.z_coordinates = z
r.dimensions = len(x), len(y), len(z)
#获取前6个点
for n in range(6):
    print(r.get_point(n))
