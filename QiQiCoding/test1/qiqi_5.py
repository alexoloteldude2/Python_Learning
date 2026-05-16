#for num in range (1,101):
#    if (num%7!=0):
#        continue
#    else :
#        print("the numbers are ",num)

tri=0
enter=input("enter password: ")
password="3345"
while (password!=enter):
    tri+=1
    if tri>=3:
        print("your password is locked pls try again later")
        break  
    enter= input("wrong password pls try again: ")


if (tri<3):
    print ("your password is corect")

    
    