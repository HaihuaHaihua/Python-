##Mayavi库入门
'''
mlab处理图像可视化和图像操作
    绘图、图形控制、图形修饰、相机控制、Mlab管线控制
api操作管线对象、窗口对象
    管线基础对象、主视窗和UI对象

Mayavi的管线(mlab.show_pipeline( ) )
    层级
        Engine: 建立和销毁 Scenes
        Scenes: 多个数据集合Sources
        Filters: 对数据进行变换
        Module Manager: 控制属性 （颜色等）
        Modules: 最终数据的表现形式
    对象
         Mayavi Scene: 场景 最顶层对象
             GridSource: scalars mesh图形表面每个点个数值
                 PolyDataNormals: 数据源GridSource的法向量
                     Colors and legends: 改变标量对应的颜色
                         Surface:
    程序配置属性：
        1.获得场景对象 mlab.gcf( )
        2.通过各对象的children属性，在管线中找到需要修改的对象
        3.配置窗口有多个选项卡，属性需要一级一级获得
'''
from mayavi import mlab
from numpy import pi,sin,cos,mgrid

'''
x = [[-1,1,1,-1,-1],[-1,1,1,-1,-1]]
y = [[-1,-1,-1,-1,-1],[1,1,1,1,1]]
z = [[1,1,-1,-1,1],[1,1,-1,-1,1]]

s = mlab.mesh(x,y,z)
mlab.show( )
'''
 
#建立数据
dphi, dtheta = pi/250.0, pi/250.0
[phi,theta] = mgrid[0:pi+dphi*1.5:dphi,0:2*pi+dtheta*1.5:dtheta]
m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
x = r*sin(phi)*cos(theta)
y = r*cos(phi)
z = r*sin(phi)*sin(theta)
 
#对该数据进行三维可视化
s = mlab.mesh(x, y, z,representation='surface',line_width=1.0) #representation 参数 绘制的表现形式
#mlab.show()
t = mlab.gcf( ) #scene对象
print(t)
print(t.scene.background) #场景背景色
source = t.children[0]  #Scene的子节点GridSource对象
print(source.name)
print(repr(source.data.points)) #输出GridSource的坐标
print(repr(source.data.point_data.scalars)) #每个点对应的标量数组
manager = source.children[0]
colors = manager.children[0]
colors.scalar_lut_manager.lut_mode = 'Blues' #改变标量对应的颜色
colors.scalar_lut_manager.show_legend = True #显示颜色与标量之间对应关系条
surface = colors.children[0]
surface.actor.property.representation = 'wireframe' #形式
surface.actor.property.opacity = 1 #透明度
mlab.show( )
