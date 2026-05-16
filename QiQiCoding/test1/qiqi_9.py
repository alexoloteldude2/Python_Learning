#定义一个累加函数，用户输入一个奇数N,计算1+3+5+7+......+N的和
Lastnum=int(input("input your last number: "))
Firstnum=int(input("input your first number: "))
valueDif=int(input("your numbers intervals: "))
Num=(Lastnum-Firstnum)//valueDif+1
print("your total numbers are: ",Num)

#定义一个累加函数，用以计算1+2+…..100的和
firstNum=int(input("your first number: "))
lastNum=int(input("your last number: "))
totalNum=int(input("you have how much numbers: "))
num=(firstNum+lastNum)*totalNum//2
print("your answer is: ",num)

#写一个函数，判断用户传入的字符串对象长度是否大于5
numm=len(input("input your number pls: "))
if numm>5:
    print("OVERLOADED")
else:
    print("good job of not overloading")

#定义一个累乘函数，用户输入一个偶数N,计算2*4*6*……N的积
lasnum=int(input("input your last number: "))
n=lasnum/2
def fun(n):
    result = 1  
    for i in range (1,int(n)+1):
        result *= i
    return result
ans=2**n*fun(n)
print(ans)