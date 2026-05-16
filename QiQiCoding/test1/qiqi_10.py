# #编写一个函数，用输入的参数打印爱心（结果如图1）
# def heart(letter):
#     print("   ",letter,"     ",letter)
#     print(" ",letter,letter,letter," ",letter,letter,letter)
#     print(letter,letter,letter,letter,letter,letter,letter,letter,letter)
#     print(" ",letter,letter,letter,letter,letter,letter,letter)
#     print("   ",letter,letter,letter,letter,letter)
#     print("     ",letter,letter,letter)
#     print("       ",letter)
# ans1=heart('❤️')
# print(ans1)

# #编写一个函数计算零钱的总面值，包括五元、十元和一百元。函数应当返回这些硬币的总面值。然后编写一个程序调用这个函数。程序运行时应当得到类似下面的输出：（结果如图2）
# def money():
#     i1=float(input("how much 5¢ coins: "))
#     i2=float(input("how much 10¢ coins: "))
#     i3=float(input("how much 20¢ coins: "))
#     i4=float(input("how much 50¢ coins: "))
#     i5=float(input("how much $1 coins: "))
#     ans=i1*0.05+i2*0.1+i3*0.2+i4*0.5+i5
#     return ans
# ans2=money()
# print(ans2)

# #定义一个函数来向家人传达节日祝福。
# def cheer(name,msg):
#     print(name,"wish you you'll",msg)
#     return name,msg
# ans3=cheer("mom","be good at work")

# #定义两个参数的函数，通过参数控制向不同家庭成员传达祝福。

# #定义三个参数的函数，通过参数控制向不同家庭成员传达不同节日的祝福
# def cheer(name,msg):
#     print(name,"wish you you'll",msg)
#     return name,msg

multi=lambda a,b:a*b
print(multi(2,1))

div=lambda a,b:a/b
print(div(2,1))

mul=lambda a,b,c:(a+8)*b-c
print(mul(1,2,3))

