##图像与数组的关系
'''
图像的数组表示
    RGB三个颜色通道的变化和叠加得到各种颜色
    red green blue 范围均为0~255

    PIL  pillow库 from PIL import image
        image对象代表一个图像（计算机中图像就是由像素组成的二维矩阵，每一个像素是一个RGB值）
        所有可以用numpy库的数组来表示一个图像

图像的变换
    读入图像 并用数组表示    获取RGB值   保存为新的文件
'''
from PIL import Image
#Image 对象 区分大小写 image 报错
import numpy as np

im = np.array(Image.open("C:/Users/regul/Pictures/lufei.png"))
#C:/Users/regul/Pictures/lufei  这里没有文件格式 要标明文件格式后缀  .png  .jpg .txt
#C:\Users\regul\Pictures\lufei.png   Windows默认路径格式 为'\'   Python路径格式为 '/'
#image.open() 用image图像的open方法打开图像路径
print(im.shape, im.dtype)
#三维数组 高度 宽度 像素的RGB值 uint8

b = [255, 255, 255] - im   #计算RGB的补值
ima = Image.fromarray(b.astype('uint8'))  #fromarray() 生成一个新的图像对象
ima.save("C:/Users/regul/Pictures/lufei2.png") #将新的图像保存

#convert('L') 将彩色的图片转化为灰度图片
imh = np.array(Image.open("C:/Users/regul/Pictures/lufei.png").convert('L'))
c = 255 - imh #灰度图片不存在 RGB值 只有灰度值 一维数组
#c = (100/255)*imh + 150 区间变换 淡色灰度
#c = 255*(imh/255)**2   像素平方  深色灰度
imh2 = Image.fromarray(c.astype('uint8'))
imh2.save("C:/Users/regul/Pictures/lufei3.png")

#手绘效果
'''
1黑白灰色
2边界线条较重
3相同或者相近色彩趋于白色
4略带光源效果

'''
