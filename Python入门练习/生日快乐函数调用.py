def happy():
    print("happy birthday to you!")
    return None

def sing(person):
    happy()
    happy()
    print("happy birthday, dear ", person+"!")
    happy()
    print() #python3.0可以直接输出空行
    
def main():
    sing("Mike")
    sing("Anna")
    sing("Lee")
    #return语句是程序退出的位置，并返回函数调用的位置 无return默认return none
    
main()
