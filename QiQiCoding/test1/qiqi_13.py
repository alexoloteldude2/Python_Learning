class Bird:
    def __init__(self,color):
        self.__color__=color
    def say(self):
        print("IM TALKING") 

myBird=Bird("red")
print(myBird.__color__)
myBird.say()

class Parrot(Bird):
    def __init__(self, color):
        super().__init__(color)
    def say(self,word):
        print("I AM A",self.__color__,"PARROT. I CAN SAY THESE WORDS:",word)
myParrot=Parrot("lime")
myParrot.say("HI! BYE! GOODMORING! GOODAFTERNOON! GOODNIGHT! SWEET DREAMS!")
        