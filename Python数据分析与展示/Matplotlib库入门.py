##matplotlib库的使用
'''
matplotlib.pyplot 绘制各类可视化图形的子库
    import matplotlib.pyplot as plt

pyplot的绘图区域（全局绘图区域中创建一个分区体系 形成子绘图区）
    plt.subplot(横轴区域数量,纵轴区域数量,当前绘图区 定位绘图区域)

自定义子绘图区
 1.第一种方法
    plt.subplot2grid((3,3),(1,0),colspan=2,rowspan=2)
    (3,3) 类似subplot 形成一个3x3的基础子区
    (1,0) 选定起始的基础子区 第1行 第0列的子区
    colspan=2 列方向上包含自身延伸2个单位
    rowspan=2 行方向上包含自身延伸2个单位
        plt.subplot2grid((3,3),(0,0),colspan=3)   第一行三个组成一个子区
        plt.subplot2grid((3,3),(1,0),colspan=2)
        .....
 2.第二种方法
     improt matplotlib.gridspec as gridspec
     gs = gridspec.GridSpec(3,3)  3x3基础子区
     ax1 = plt.subplot(gs[0, :])  第一行三个组成一个子区
     ax2 = plt.subplot(gs[1, 1])
     ....

plt.plot(x, y, format_string, 更多（x,y,fromat_string）)
        x y 坐标数据 列表或者数组类型
        fromat_string 控制曲线的格式
        绘制多条曲线 x y fromat_string 三个参数重复

中文显示
    一、pyplot并不默认支持中文显示，需要修改matplotlib的rcParams属性实现字体修改
        import matplotlib
        matplotlib.rcParams['font.family']='字体格式'
    rcParams属性包括 1.font.family 字体名称 2.font.style 字体风格斜体('italic')  3.font.size 字体大小(整数字号)
    第一种方法会改变整个图表的字体
    二、在用中文输入的地方增加一个中文属性 fontproperties='字体格式'

pyplot文本显示
    xlabel() ylabel() 对 xy轴增加文本标签
    title() 标题文本
    text() 在图形任意位置增加文本
    annotate() 在图形中增加带箭头的注解
'''

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

#保存文件
plt.subplot(333) #分区绘制 subplot(211) 参数逗号可要可不要 
plt.plot([3,4,4,5,3]) # 列表参数
plt.ylabel("first")  #标签
plt.savefig('firstPlt',dpi = 600)  #保存文件 默认为png格式，可以通过dpi(每英寸空间像素点数量)修改输出质量
#plt.show()

#坐标轴绘制
plt.subplot(336)
#plot()函数应该有很多参数 坐标数据 线条类型 线条颜色 等。。。。 ' r--' 表示红色虚线
plt.plot([0, 2, 4, 6, 8],[3, 1, 4, 5, 2,], 'r--') #两个列表参数 分别对应xy轴点 plot(x,y)
plt.ylabel('Grade')
plt.axis([-1, 10, 0, 6]) #坐标系绘制 .axis([x轴起点，x轴终点，y轴起点，y轴终点] )

#多条曲线绘制
plt.subplot(339)
a = np.arange(10)
plt.plot(a , a*1 , 'rv-', a , a*2 ,'b-.', a , a*3 ,'*', a , a*4 ,'#008000')
#第三参数 format_string
#曲线颜色 可以是 颜色单词首字母 也可以是 RGB值'#008000'  也可以是灰度值'0.8'
#曲线风格 一般五种 可以是 '-'实线 '--'破折线 '-.'点划线 ':'点虚线 ' '空格 无线条
#曲线点标记 '.' 点标记 'v'倒三角标记
#fromat_string 可以通过参数控制 color='green' linestyle='dashed' marker='o' 等等参数可以对曲线进行精细微调

#中文显示1
plt.subplot(331)
matplotlib.rcParams['font.family']='STSong'
matplotlib.rcParams['font.size']=8
b = np.arange(0.0,5.0,0.02)
plt.plot(b,np.cos(2*np.pi*b),color='green')
plt.ylabel('纵轴：振幅')
plt.xlabel('横轴：时间')

#中文显示2
plt.subplot(334)
c = np.arange(0.0,5.0,0.02)
plt.plot(c,np.cos(2*np.pi*c),color='blue')
plt.ylabel('纵轴：振幅',fontproperties='SimHei',fontsize=8)
plt.xlabel('横轴：时间',fontproperties='SimHei',fontsize=8)

#文本显示
plt.subplot(337)
d = np.arange(0.0,5.0,0.02)
plt.plot(d,np.cos(2*np.pi*d),color='yellow')
plt.ylabel('纵轴：振幅',fontproperties='SimHei',fontsize=6)
plt.xlabel('横轴：时间',fontproperties='SimHei',fontsize=6)
# $ ... $ 用$符引用一部分 latex格式 的文本
plt.title(r'正弦波 $y=cos(2\pi x)$',fontproperties='SimHei',fontsize=6)
# plt.text(2 ,1 ,r'$\mu=100$', fontsize=4 ) #text(x,y,content) 显示的位置(x,y) 显示内容为content
plt.annotate(r'$\mu=100$', xy=(2,1),  xytext=(3,1.5), arrowprops=dict(facecolor='black', shrink=0.1,width=0.5))
#annotate(内容，箭头位置，内容位置，箭头属性)
plt.axis([-1, 6, -2, 2 ])
plt.grid(True) #加入网格

plt.show()


