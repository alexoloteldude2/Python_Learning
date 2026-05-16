import random
secret=random.randint(1,11)
print("guess the number")
guess=0
time=3
while(guess!=secret)and(time>0):
    temp=input()
    guess=int(temp)
    time=time-1
    if guess==secret: 
        print ("you got it")
    else:
        if guess>secret: 
            print ("too big")
        else:
            print("too small")
        if time>0: 
            print("try again next time")
        else: 
            print("you finished your tries, try again next time")
print("lets dont play the game has ended")
print ("the number is ",secret)