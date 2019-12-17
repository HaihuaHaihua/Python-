##TVTK数据加载
'''
TVTK读取模型
    1.obj文件、ply文件、stl文件读取
      vtkOBJReader、vtkPLYReader、vtkSTLReader ---> vtkAbstractPolyDataReader
      ---> vtkPolyDataAlgorithm ---> vtkAlgorithm ---> vtkObject
    2.Plot3D文件 MultiBlock数据读取
        网格（XYZ文件） 空气动力学结果（Q文件） 通用结果文件
        vtkMultiBlockPLOT3DReader ---> vtkMultiBlockDataSetAlgorithm
        ---> vtkAlgorithm ---> vtkObject

         plot3d = tvtk.MultiBlockPLOT3DReader(
            xyz_file_name="combxyz.bin",#网格文件
            q_file_name="combq.bin",#空气动力学结果文件
            scalar_function_number=100,#设置标量数据数量
            vector_function_number=200#设置矢量数据数量
            )   #一共四个参数
'''
'''
from tvtk.api import tvtk
from Tvtkfunc import ivtk_scene,event_loop   #导入自己写的Tvtkfunc文件

#读取stl文件
s = tvtk.STLReader(file_name = "python.stl") 
m = tvtk.PolyDataMapper(input_connection = s.output_port)
a = tvtk.Actor(mapper = m)
 #创建观察窗口
win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()

'''
#读取Plot3D文件 MultiBlock数据读取
from tvtk.api import tvtk

def read_data( ):
    #读入数据
     plot3d = tvtk.MultiBlockPLOT3DReader(
            xyz_file_name="combxyz.bin",#网格文件
            q_file_name="combq.bin",#空气动力学结果文件
            scalar_function_number=100,#设置标量数据数量
            vector_function_number=200#设置矢量数据数量
            )
     plot3d.update( ) #实际操作读取数据
     return plot3d

plot3d = read_data( ) #调用函数
grid = plot3d.output.get_block(0) #获取网络数据及 StructureGrid

#网格范围
print(grid.dimensions)
#网格点的坐标
print(grid.points.to_array())
#网格点数据种类
print(grid.point_data.number_of_arrays)
