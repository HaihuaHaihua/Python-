#改变函数参数值
def addInterest(balance,rate):
    #函数形参接收了实参数据，但是无法改变实参
    #newBalance=balance*(1+rate)
    #balance=newBalance
    #return newBalance 产生一个返回值可以改变实参的值
    for i in range(len(balance)):
        balance[i]=balance[i]*(1+rate)
def main():
    #amount=1000
    amounts=[1000,105,3500,739]
    rate=0.05
    #addInterset(amount,rate)
    addInterest(amounts,rate)
    #print(amount)
    print(amounts)
    
main()
