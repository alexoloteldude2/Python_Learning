# for num in range(1,100):
#     if(num % 7 == 0):
#         continue
#     print("current number:", num)

num = 3
password = input("pls input password:")
while password != "1234":
    if(num > 1):
        num -= 1
        print("password wrong, you have",num, "times remain.")
        password = input("pls input password again:")
    else:
        print("your account is locked.")
        break

if(num > 0):
    print("Conguratuation, you are in system already.")