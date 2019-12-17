#文件处理
#open()  <variable>=open(<name>,<mode>) name:文件名
#mode:打开模式  r,w,a,  二进制文件rb,wb,ab

def main():
    #用户输入文件名
    f1= input("Enter a souce file:").strip()
    f2= input("Enter a souce file:").strip()

    #打开文件
    infile=open(f1,"r")
    outfile=open(f2,"w")

    #拷贝数据
    countLines=coutnChars=0
    for line in infile:
        countLines+=1
        countChars+=len(line)
        outfile.write(line)
    print(countLines,"Lines and",countChars,"chars copied")

    infile.close()
    outfile.close()
    
main()
