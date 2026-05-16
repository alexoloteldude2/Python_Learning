class Animal:
    def __init__(self,name,wieght,legnum,):
        self.name=name
        self.legnum=legnum
        self.wieght=wieght
ostric=Animal("ostric",2,"130")
ostric=Animal("tiger",4,"190")
print(ostric.name,ostric.wieght,ostric.legnum)





class Tools:
    def __init__(self,name,usedfor):
        self.name=name
        self.usedfor=usedfor
pencil=Tools("pencil","write")
ruler=Tools("ruler","meassure, draw straight lines")
print(pencil.name,pencil.usedfor) 
print(ruler.name,ruler.usedfor)