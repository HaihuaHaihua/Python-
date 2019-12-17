##Matplotlib的基础绘图函数
'''
pyplot的基础图标函数
    plt.plot() 坐标图
    plt.bar()  直方图
    plt.pie() 饼图
    plt.scatter(x,y) 散点图
    plt.plot_date() 数据日期
    .....

'''
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

gs = gridspec.GridSpec(2,2)

##饼图
g1 = plt.subplot(gs[0,0])
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0 , 0)  #第二部分突出o.1

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=False, startangle=90)
#pie(各部分尺寸，突出部分，各部分对应的标签，显示百分数的方式，阴影，起始角度)
plt.axis('equal')  #让xy轴上的值相等

##直方图
g2 = plt.subplot(gs[0,1])
np.random.seed(0)
mu, sigma = 100 , 20 #均值和标准差
a = np.random.normal(mu, sigma, size = 100)

plt.hist(a, 20, normed=1, histtype='stepfilled', facecolor='g', alpha=0.75)
#hist(数据值，bin值即直方图个数 高度由数组中范围内元素个数决定，normed=1 出现的概率 =0 是y值代表个数， 绘制类型，颜色，比例)
plt.title('直方图', fontproperties='SimHei')

##极坐标图
#g3 = plt.subplot(gs[1,0])
N = 20  #数据个数
theta = np.linspace(0.0 , 2*np.pi, N , endpoint=False) #N等分0-360度
radii = 10 * np.random.rand(N) #每个角度对应的值
width = np.pi / 4 * np.random.rand(N) #每等分宽度值

#g3 = plt.subplot(223, projection = 'polar') #面向对象绘图 形成对象ax 
g3 = plt.subplot(gs[1,0], projection = 'polar')
bars = g3.bar(theta, radii, width=width, bottom=0.0)
#bar(left绘制极坐标系颜色区域的起始位置,height从中心点到边缘的绘制长度,width区域的面积 )

#设定每个区域的颜色
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
    bar.set_alpha(0.5)

##散点图
#fig, g4 = plt.subplots(224, 224)    #subplots() 怎么用？
#g4 = plt.subplot(224) #创建一个绘图对象
g4 = plt.subplot(gs[1,1])
g4.plot(10*np.random.randn(100),  10*np.random.randn(100), '*') #g4对象调用plot函数 绘制图像
g4.set_title('Simple Scatter') #调用set_title() 函数设置标题 

plt.show()

