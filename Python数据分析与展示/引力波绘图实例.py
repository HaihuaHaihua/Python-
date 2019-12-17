##引力波实例
'''
考虑一下能不能用爬虫爬取 引力波数据源
http://python123.io/dv/grawave.html
http://python123.io/dv/H1_Strain.wav
http://python123.io/dv/L1_Strain.wav
http://python123.io/dv/wf_template.txt

可以在引力波官网深度了解 python对引力波的绘图
'''
import numpy as np #科学计算库
import matplotlib.pyplot as plt  #绘图库
from scipy.io import wavfile  #读取波形的库
import matplotlib.gridspec as gridspec

#读取文件
rate_h, hstrain = wavfile.read(r"H1_Strain.wav","rb") #出现转义字符是前缀r表示使用原始字符
rate_l, lstrain = wavfile.read(r"L1_Strain.wav","rb")
reftime,ref_H1 = np.genfromtxt('wf_template.txt').transpose() #时间序列和引力波数据

htime_interval = 1/rate_h
ltime_interval = 1 / rate_l

htime_len = hstrain.shape[0]/rate_h
htime = np.arange(-htime_len/2, htime_len/2, htime_interval)
ltime_len = lstrain.shape[0]/rate_l
ltime = np.arange(-ltime_len/2, ltime_len/2, ltime_interval)

#绘制
plt.figure(figsize=(12,6)) #创建图像板
gs = gridspec.GridSpec(2,2)

#绘制H1 Strain
plth = plt.subplot(gs[0,0])
plth.plot(htime, hstrain, 'b')
#plth.xlabel("Time/s")
plth.set_xlabel("Time/s")
plth.set_ylabel("H1 Strain")
plth.set_title("H1 Strain")

#绘制L1 Strain
pltl = plt.subplot(gs[0,1])
pltl.plot(ltime, lstrain, 'g')
pltl.set_xlabel("Time/s")
pltl.set_ylabel("L1 Strain")
pltl.set_title("L1 Strain")

#绘制L1 Strain
pltref = plt.subplot(gs[1,:]) #自定义画子区  1.  subplot2grid((3,3),(1,0),colspan=?,rolspan=?) 使用 colspan rolspan 延伸 2. gs = gridspec.GridSpec(3,3)   ax= plt.subplot(gs[1,:2]) 使用冒号延伸
pltref.plot(reftime, ref_H1, 'g')
pltref.set_xlabel("Time/s")
pltref.set_ylabel("Template Strain")
pltref.set_title("Template")

plt.tight_layout() #自动调整图像边缘 
plt.savefig("Strain")
plt.show()




