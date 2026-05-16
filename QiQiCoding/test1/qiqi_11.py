class Animal:
    def __init__(self,name,weight,legNum):
        self.name=name
        self.weight=weight
        self.legNum=legNum
    def run (self):
        print("I'M RUNNING")
        print(self.name)
dog=Animal("dog",10,4)
tiger=Animal("tiger",300,4)
ostrage=Animal("osrage",100,2)
tiger.name="kingOfJungles"
print(tiger.name,tiger.weight,tiger.legNum)
tiger.run()