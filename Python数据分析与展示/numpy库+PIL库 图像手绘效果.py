#图像转手绘实例
'''
1黑白灰色
2边界线条较重
3相同或者相近色彩趋于白色
4略带光源效果

'''

from PIL import Image
import numpy as np

a = np.array(Image.open("C:/Users/regul/Pictures/lufei.png").convert('L')).astype('float')
##利用像素之间的梯度值和虚拟深度值对图像重构 根据灰度变化来模拟人觉视觉的明暗程度
depth = 10.         #预设深度值为10 取值范围为0--100
grad = np.gradient(a)  #取图像灰度的梯度值
grad_x , grad_y = grad  #分别取横纵图像的x和y方向梯度值
grad_x = grad_x * depth / 100.
grad_y = grad_y * depth / 100.  #根据深度调整x和y方向的梯度值
#构造x和y轴梯度的三维归一化单位坐标系
A = np.sqrt(grad_x**2 + grad_y**2 +1.)
# uni x y z 表示单位法向量
uni_x = grad_x / A
uni_y = grad_y / A
uni_z = 1. / A
'''
1.设计一个位于图像斜上方的虚拟光源
2.光源相对于图像的俯视角 vec_el  方位角 vec_az
3.建立光源对个点梯度值的影响函数
4.运算出个点的新像素值

depth 物体的深度

'''
vec_el = np.pi / 2.2  # 光源的俯视角度 ， 弧度值
vec_az = np.pi / 4. # 光源的方位角度，弧度值
dx = np.cos(vec_el)*np.cos(vec_az) # 光源对x 轴的影响程度
dy = np.cos(vec_el)*np.sin(vec_az)  # 光源对y 轴的影响程度
dz = np.sin(vec_el)  #光源对z 轴的影响程度

b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)  #光源归一化
b = b.clip(0,255) #避免数据越界，将生成的灰度值裁剪值0 - 255 区间

im = Image.fromarray(b.astype('uint8')) #新建图像
im.save("C:/Users/regul/Pictures/lufei4.png")
