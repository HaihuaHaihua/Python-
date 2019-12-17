#递归函数fact() python中最多递归次数为900
#递归函数的特征，有一个或者多个基例的函数不需要再次递归；所有的递归链都要以一个基例结尾
#基例：递归执行到基例时，递归调用结束
def reverse(s):
    #创建一个基例使得递归可以停止
    if(s==""):
        return s
    else:
        return reverse(s[1:])+s[0]
def main():
    reverse("hello")

main()
        
