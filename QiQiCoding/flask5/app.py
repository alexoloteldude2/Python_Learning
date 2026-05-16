from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
app=Flask(__name__)

prefix = 'sqlite:////'

db = SQLAlchemy()
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'myFirstDB.db')

db.init_app(app)

class User(db.Model):  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键
    name = db.Column(db.String(20))  # 名字

class Movie(db.Model):  
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)  # 主键
    name = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份


@app.route('/')
@app.route('/home')
def index():
    movies=db.session.query(Movie).all()
    return render_template("home.html",movies=movies)

@app.errorhandler(404)  
def page_not_found(e):  
    return render_template('404.html'), 404  

@app.context_processor
def inject_user(): 
    user = db.session.query(User).first()
    return dict(user=user) 






