import turtle

def main():
    p = turtle()
    p.color("green")
    p.pensize(5)
    p.hideturtle()
    p.getscreen().tracer(30,0)
    p.left(90)#tutle默认方向是ease东或者说是正右方
    
    p.penup()
    p.goto(200,-200)
    p.pendown()

    t=tree([p],110,65,0.6375)


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
main ()
