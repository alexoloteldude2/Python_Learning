chatBook={}

def create():
    pass

def add(nickname,phonenum):
    chatBook[nickname]=phonenum

def update(nickname,phonenum):
    chatBook[nickname]=phonenum

def delete(nickname):
    del chatBook[nickname]

def empChat():
    chatBook.clear()

def showCurBook():
    for curkey in chatBook:
        print(curkey,chatBook[curkey])