from flask import Flask,url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/home')
@app.route('/index')
def helloHome():
    return 'Welcome to My Site!'

@app.route('/user/<name>')
def user_page(name):
    return escape(name)+' is using current page'

@app.route('/test')
def test_url_for():
    print(url_for('hello'))  
    print(url_for('helloHome'))  
    print(url_for('user_page', name='qiqi')) 
    print(url_for('test_url_for'))  

    return 'Test page'
