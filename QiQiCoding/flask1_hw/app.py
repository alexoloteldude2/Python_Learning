from flask import Flask

app=Flask(__name__)
@app.route('/')
def hi():
    return ("HI")

@app.route('/second')
def hi2():
    return '<h5>HI BYE</h5><img src=https://static.vecteezy.com/system/resources/previews/010/313/698/original/funny-emoji-and-laugh-file-png.png'

@app.route('/third/<name>')
def hi3(name):
    return name,"is definatly not online ;)"
