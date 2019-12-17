#学生成绩计算 类的应用
#类的创建 class classname[(父类名)]：
#类的构造函数 _init_ 析构函数 _del_
class Student:
    def __init__(self,name,hours,qpoints):
        self.name=name
        self.hours=float(hours)
        self.qpoints=float(qpoints)
    def getName(self):
        return self.name
    def getHours(self):
        return self.hours
    def getQPoints(self):
        return self.qpoints
    def gpa(self):
        return self.qpoints/self.hours
    #以上创建学生类

def makeSutdent(infoStr):
    name,hours,qpoints=infoStr.split("\t")
    return Student(name,hours,qpoints)

    #主函数
def main():
    #打开输入文件
    filename=input("Enter name the grade file: ")
    infile=open(filename,'r')
    #设置文件中第一个学生的记录为best
    best=makeSutdent(infile.readline())

    #处理文件剩余行数据
    for line in infile:
        #将每一行数据转换为一个记录
        s=makeSutdent(line)
    #如果该学生目前的Gpa最高，则记录
    if s.gpa()>best.gpa():
        best=s
    infile.close()

    #打印GPA最高的学生信息
    print("The best student is: ",best,getName())
    print("hours:",best.getHours())
    print("GPA:",best.gpa())

if __name__=='__main__':
        main()
