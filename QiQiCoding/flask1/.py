from flask import Flask
from markupsafe import escape


app=Flask(__name__)
@app.route('/')
def hi():
    return ("HI")

@app.route('/second')
def hi2():
    return '<h5>HI BYE</h5><img src=https://static.vecteezy.com/system/resources/previews/010/313/698/original/funny-emoji-and-laugh-file-png.png'

@app.route('/third/<name>')
def hi3(name):
    return escape (name),"is definatly not online ;)"
