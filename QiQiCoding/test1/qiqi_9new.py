#Q1
def sum(firstnum,diff,totalnum):
    lastnum=firstnum+(totalnum-1)*diff
    result=(firstnum+lastnum)*totalnum/2
    return result
ans1=sum(1,1,100)
print(ans1)

ans2=sum(1,2,100)
print(ans2)

def multiplication(firstnum,diff,totalnum):
    result=firstnum
    for i in range(1,totalnum):
        result*=firstnum+i*diff
    return result
ans3=multiplication(2,2,5)
print(ans3)

def checkLength(mystring):
    length=len(mystring)
    if length>=5:
        print("OVERLOADED")
    else:
        print("your massage was:",mystring)
mystring=input("pls input a random massage: ")
checkLength(mystring)
