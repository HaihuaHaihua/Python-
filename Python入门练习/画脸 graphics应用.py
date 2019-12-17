from graphics import *

win = GraphWin()
face = Circle(Point(100,95),100)#画圆 圆心+半径
leftEye = Circle(Point(80,80),5)
leftEye.setFill("yellow")#填充色
leftEye.setOutline("red")#边缘线
rightEye = Circle(Point(120,80),5)
rightEye.setFill("yellow")
rightEye.setOutline("red")
mouth = Line(Point(80,110),Point(120,110))#两个点的连线

face.draw(win)
mouth.draw(win)
leftEye.draw(win)
rightEye.draw(win)
