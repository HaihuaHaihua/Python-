#字典
#针对非序列集合 使用<键><值>对的方法

import turtle

##全局变量##
#词频序列显示个数()
count=10
#单词频率数值作为y轴数据
data=[]
#单词数据作为x轴数据
words=[]
#y轴显示被放大倍数 可以根据词频数量调节
yScale=6
#x轴显示被放大倍数 可以根据count数量调节
xScale=30

#####################绘图
#从点(x1,y1)到(x2,y2)绘制
def drawLine(t,x1,y1,x2,y2):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)

#在坐标(x,y)处写文字
def drawText(t,x,y,text):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.write(text)

def drawGraph(t):
    #绘制坐标轴
    drawLine(t,0,0,360,0)
    drawLine(t,0,300,0,0)

    #x轴 坐标及描述
    for x in range(count):
        x=x+1
        drawText(t,x*xScale-4,-20,(words(x-1)))
        drawText(t,x*xScale-4,data(x-1)*yScale+10,data(x-1))
    drawBar(t)

#绘制柱体
def drawBectangle(t,x,y):
    x=x*xScale
    y=y*yScale
    drawLine(t,x-5,0,x-5,y)
    drawLine(t,x-5,0,x+5,y)
    drawLine(t,x+5,0,x+5,y)
    drawLine(t,x+5,0,x-5,y)

#绘制多柱体
    def drawBar(t):
        for i in range(count):
            drawRectangle(t,i+1,data[i])
#############################

#对文本每一行计算词频
def processLine(Line,wordCounts):
    #用空格替换标点符号
    line=replacePunctuations(line)
    #从每一行中获取每一个词
    words=line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word]+=1
        else:
            wordCounts[word]=1

#用空格替换标点
def replacePunctuations(line):
    for ch in line:
        if ch in"!@#$%^&*()_+-=~<>?:[]\{}|:;<>":
            line = line.replace(ch," ")
    return line

def main():
    #用户输入一个文件名
    filename=input("enter a filename:").strip()
    infile=open(filename,"t\r")
    
    #建立空字典
    wordCounts={}
    for line in infile:
        processLine(Line.lower(),wordCounts)
        
    #从字典中获取数据对
        pairs=list(wordCounts.items())
        
    #列表中的数据交换位置，数据对排序
        items=[[x,y]for (y,x)in pairs]
        items.sort()
        
    #输出count个数 词频的结果
        for i in range()
    #根据词频结果绘图
    #调用main()函数
            
