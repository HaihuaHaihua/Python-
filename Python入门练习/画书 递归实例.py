import turtle
import random

def tree(plist,l,a,f):
    """
    plist存放一组turtle对象列表
    l=length a=angle f为不同层树枝长度比例
    """
    if l>5:
        lst=[]#turtle对象的空列表
        for p in plist:
            p.forward(l)
            q=p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)#将元素p添加到turtle对象列表中
            lst.append(q)
        tree(lst,l*f,a,f)
"""
def randomNum():
    return random.randint(20,600)

import random 产生随机数  random.randint整型 random.uniform浮点型（a,b）随机数的范围
"""
#完成对turtle对象的设置
def maketree(x,y):
    p=turtle()
    p.color("green")
    p.pensize(5)
    p.hideturtle()
    p.getscreen().tracer(30,0)
    p.left(90)#tutle默认方向是ease东或者说是正右方
    """
    x=randomNum()
    y=randomNum()
    """
    #下面三句语句 想把pen收起来在移动到指定位置后再开始画
    p.penup()
    p.goto(x,y)
    p.pendown()

    t=tree([p],110,65,0.6375)

def main():
"""
    color=["green","red","black","blue","yellow"]
    for i in range(4):
        maketree(color[i])
"""
    maketree(20,200)
    maketree(40,400)

main()
