##mlab基础-绘图函数
'''
Points3d( ) 绘制点图形 Plot3d( )绘制线图形

'''

import numpy as np
from mayavi import mlab

##绘制点图形 points3d( )
'''
#建立数据
t = np.linspace(0, 4 * np.pi , 20) #0-4pi之间建立20个等差数列数组

x = np.sin(2*t)
y = np.cos(t)
z = np.cos(2*t)
s = 2 + np.sin(t) # x y z 坐标点的标量值
#数据可视化
points = mlab.points3d(x, y, z, s, colormap='Red', scale_factor=.25) #scale_factor为放缩比例
mlab.show(stop = False ) #mlab.show( ) 建立一个简单的GUI对话框  stop 参数表示循环是否停止
'''
##绘制线图形 plot3d( )
# plot3d( ) 参数多了 对线条描述的 tube_radius 线条截面半径  tube_sides 线条分段数 默认6
'''
#建立数据
n_mer, n_long = 6, 11
dphi = np.pi / 1000.0
phi = np.arange(0.0, 2 * np.pi + 0.5 * dphi, dphi)
mu = phi * n_mer

x = np.cos(mu) * (1 + np.cos(n_long * mu / n_mer)*0.5)
y = np.sin(mu) * (1 + np.cos(n_long * mu / n_mer)*0.5)
z = np.sin(n_long * mu / n_mer) * 0.5
#数据可视化
l = mlab.plot3d(x, y, z, np.sin(mu), tube_radius=0.025, colormap='Spectral')
mlab.show( )
'''
##用二维numpy数组数据绘制图像

# imshow( ) 绘图
'''
#建立数据
s = np.random.random((100,100))

#数据可视化
img = mlab.imshow(s, colormap='gist_earth')
mlab.show( )
'''

#surf( ) 绘图 求解曲面
'''
def f(x, y):
    return np.sin(x - y)+np.cos(x + y)
x, y = np.mgrid[-7. : 7.05 : 0.1, -5. : 5.05 : 0.05] #建立 x y 的数组
s = mlab.surf(x, y, f)
mlab.show( )
'''
#contour_surf( ) 绘图 求解等值线
'''
def f(x, y):
    return np.sin(x - y)+np.cos(x + y)
x, y = np.mgrid[-7. : 7.05 : 0.1, -5. : 5.05 : 0.05] #建立 x y 的数组
s = mlab.contour_surf(x, y, f)
mlab.show( )
'''

##用三维numpy数组数据绘制图像

#contour3d( ) 三维体数据等值面 数据可视化
'''
x, y, z = np.ogrid[-5 : 5 : 64j, -5 : 5 : 64j, -5 : 5 : 64j]
scalars = x*x + y*y + z*z
obj = mlab.contour3d(scalars, contours=8, transparent = True) #transparent参数 图像是否可以透明表示
mlab.show( )
'''
#quiver3d( ) 三维矢量数据可视化(arrow箭头)
x, y, z = np.mgrid[-2 : 3, -2 : 3, -2 : 3]
r = np.sqrt(x ** 2 + y ** 2 + z ** 4)
u = y *np.sin(r) / (r + 0.001)
v = -x * np.sin(r) / (r + 0.001)
w = np.zeros_like(z)

obj = mlab.quiver3d(x, y, z, u, v, w, line_width=3, scale_factor=1)
mlab.show( )
#flow( ) 向量场粒子轨迹描述
