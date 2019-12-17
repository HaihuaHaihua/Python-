##管线与数据加载
'''
管线技术 Pipeline(流水线)
    可视化管线  原始数据到图形数据  PolyData -- PolyDataMapper
    图形管线  图形数据到绘制图形
    数据--数据预处理--数据映射--绘制Rendering--显示Displaying

使用IVTK观察管线
    from tvtk.tools import ivtk
    from pyface.api import GUI
'''

'''
from tvtk.api import tvtk
from tvtk.tools import ivtk
from pyface.api import GUI

s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
m = tvtk.PolyDataMapper(input_connection=s.output_port)
a = tvtk.Actor(mapper=m)

#创建一个Crust窗口的对象
gui = GUI( )
win = ivtk.IVTKWithCrustAndBrowser( )
win.open( )
win.scene.add_actor(a)

#用pyface将管线子窗口放到主窗口上
dialog = win.control.centralWidget( ).widget(0).widget(0)
from pyface.qt import QtCore
dialog.setWindowFlags(QtCore.Qt.WindowFlags(0x00000000))
dialog.show( )

#开始界面消息循环
gui.start_event_loop( )
'''
'''
##对程序进行封装
from tvtk.api import tvtk

##创建多文件 进行封装
#Tvtkfunc.py

#创建ivtk窗口
def ivtk_scene(actors):
    from tvtk.tools import ivtk
    win = ivtk.IVTKWithCrustAndBrowser( )
    win.open( )
    win.scene.add_actor(a)
    dialog = win.control.centralWidget( ).widget(0).widget(0)
    from pyface.qt import QtCore
    dialog.setWindowFlags(QtCore.Qt.WindowFlags(0x00000000))
    dialog.show( )
    return win
#界面消息循环
def event_loop( ):
    from pyface.api import GUI
    gui = GUI
    gui.start_event_loop( )
'''
from tvtk.api import tvtk
from Tvtkfunc import ivtk_scene,event_loop # 从封装的Tvtkfunc.py文件 导入ivtk_scene和event_loop函数

s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
m = tvtk.PolyDataMapper(input_connection=s.output_port)
a = tvtk.Actor(mapper=m)
win = ivtk_scene(a)
win.scene.isometric_view( )
event_loop( )
