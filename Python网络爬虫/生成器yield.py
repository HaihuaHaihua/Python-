'''
yield 生成器
1.生成器是一个不断产生值的函数
2.包含yield语句的函数是一个生成器
3.生成器每次产生一个值，然后函数被冻结，在被唤醒的时候再产生一个值

yield 相对于 列表
1.更节省空间
2.响应更快
3.使用更加灵活
'''
#生成器写法
def gen(n):
    for i in range(n):
        yield i**2

for i in gen(5):
    print(i," ",end="")

print("\n")
#列表写法
def square(m):
    ls = [j**2 for j in range(m)] #先将值都计算出来存在列表中 在逐一返回
    return ls

for j in square(5):
    print(j," ",end="")
