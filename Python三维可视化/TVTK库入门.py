##TVTK入门
'''
基本三维对象
    CubeSource长方体对象
        s.x_length x轴方向长度 s.y_length s.z_length类似 s.center坐标系原点
        set/get_x_length()  设置/获取长方体对象在x轴方向的长度
        set/get_bounds() 设置/获取长方体对象的包围盒
    ConeSource立方体对象数据源 CylinderSource圆锥 ArcSource圆弧 ArrowSource箭头

显示三维对象
    ##管线与数据加载
    管线技术 Pipeline(流水线)
        可视化管线  原始数据到图形数据  PolyData -- PolyDataMapper
        图形管线  图形数据到绘制图形

        数据--数据预处理--数据映射--绘制Rendering--显示Displaying

        可视化管线 数据--数据预处理
            1.创建基本对象
            2.用PolyDataMapper 将数据转化为图形数据
        图形管线 数据映射-- 绘制 -- 显示 
            3.用Actor 创建一个实体
            4.用Renderer 创建一个渲染器
            5.用RenderWindow 创建一个绘制窗口
            6.用RenderWindowInteractor 创建交互工具  通过调整图形中Camera的位置来实现 放缩 旋转 ...

            7.用initialize() start() 启动交互
'''

from tvtk.api import tvtk

#CubeSource构造一个基本三维对象 traits封装vtk作为tvtk的对象属性
s = tvtk.CubeSource(x_length = 1.0, y_length = 2.0, z_length = 3.0)
print(s)
print(s.center) #坐标原点
#圆锥
t = tvtk.CylinderSource(height = 3.0, radius=1.0, resolution=36)
print(t)

##显示三维对象
m = tvtk.PolyDataMapper(input_connection=s.output_port) #使用PolyDataMapper(映射器)将数据转换为图形数据
a = tvtk.Actor(mapper=m) #创建一个Actor (创建一个实体)
r = tvtk.Renderer(background=(0, 0, 0)) #创建一个Renderer  (创建一个渲染器)
r.add_actor(a) #将Actor添加进去
w = tvtk.RenderWindow(size=(300, 300)) #创建一个绘制窗口
w.add_renderer(r) #将Renderer添加进去
i = tvtk.RenderWindowInteractor(render_window=w) #创建窗口交互工具
i.initialize() 
i.start() #开启交互


