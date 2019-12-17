##可视化实例
'''
标量可视化
     tvtk.ContourFilter( ) 等值面过滤器等值面对标量进行可视化
         vtkContourFliter --> vtkPloyDataAlgorithm --> vtkAlgorithm --> vtkObject
        generate_values( ) 重新绘制等值线 set_value( ) 覆盖或添加等值线
矢量可视化
    tvtk.Glyph3D( ) 符号化技术 产生可放缩 着色 箭头的符号
        vtkGlyph3D --> vtkPloyDataAlgorithm --> vtkAlgorithm --> vtkObject
        使用tvtk.MaskPoints( ) 降采样  降维使得绘制速度更快、箭头密度适中
            vtkMaskPoints --> vtkPloyDataAlgorithm --> vtkAlgorithm --> vtkObject
轮廓线可视化
    tvtk.StructuredGridOutlineFilter( ) 计算PolyData对象的外边框
        vtkStructuredGridOutlineFilter --> vtkPloyDataAlgorithm --> vtkAlgorithm --> vtkObject
        
'''
from tvtk.api import tvtk
from Tvtkfunc import ivtk_scene,event_loop

#读入数据 流体数据
plot3d = tvtk.MultiBlockPLOT3DReader(
            xyz_file_name="combxyz.bin",#网格文件
            q_file_name="combq.bin",#空气动力学结果文件
            scalar_function_number=100,#设置标量数据数量
            vector_function_number=200#设置矢量数据数量
            )
#对plot3d计算并输出数据
plot3d.update( )
#获取读取的数据集对象
grid = plot3d.output.get_block(0)

##标量可视化 等值面表示
'''
con = tvtk.ContourFilter( )
con.set_input_data(grid)
con.generate_values(10,grid.point_data.scalars.range) #以grid数据创建10个等值面
con.set_value(0, 3)  #set_value(第几个等值面，等值面的值)

m = tvtk.PolyDataMapper(scalar_range=grid.point_data.scalars.range, input_connection = con.output_port)

a = tvtk.Actor(mapper = m)
a.property.opacity = 0.3 #设置透明度
#窗口绘制
win = ivtk_scene(a)
win.scene.isometric_view( )
event_loop( )

'''

##适量数据可视化 箭头表示
'''
#mask对象实对grid数据集的数据点进行采样
mask = tvtk.MaskPoints(random_mode=True, on_ratio=50) #对数据集中的数据进行随机选取，每50个点选择一个点
mask.set_input_data(grid)

glyph_source = tvtk.ArrowSource( ) #创建箭头数据集
#glyph_source = tvtk.ConeSource( )
#对在mask采样后的PolyData数据集的每个点拷贝一个符号 并设置符号属性
glyph = tvtk.Glyph3D(input_connection = mask.output_port, scale_factor=4) #scale_factor=4 符号的共同放缩系数
#在每一个点放一个ArrowSource() 箭头
glyph.set_source_connection(glyph_source.output_port)

m = tvtk.PolyDataMapper(scalar_range=grid.point_data.scalars.range, input_connection = glyph.output_port)

a = tvtk.Actor(mapper = m)
#绘制窗口
win = ivtk_scene(a)
win.scene.isometric_view( )
event_loop( )
'''
##空间轮廓线可视化
from tvtk.common import configure_input  #导入外框计算模块

outline = tvtk.StructuredGridOutlineFilter( ) #构造外边框计算的PolyData对象
configure_input(outline, grid) #调用tvtk.common.configure_input( ) 将外框计算与grid产生关联

m = tvtk.PolyDataMapper(input_connection = outline.output_port)
a = tvtk.Actor(mapper = m)
a.property.color = 0.3, 0.3, 0.3
#窗口绘制
win = ivtk_scene(a)
win.scene.isometric_view( )
event_loop( )
