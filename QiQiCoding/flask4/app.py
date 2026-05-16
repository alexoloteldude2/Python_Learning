import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

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

with app.app_context(): 
    db.create_all()

def initTable():
    movie = Movie(
            name="One Piece",
            year="1980"
        )
    db.session.add(movie)

    movie = Movie(
            name="lion king",
        )
    db.session.add(movie)

    user = User(
        name="Qi Qi"
    )
    db.session.add(user)
    db.session.commit()
    return "db init finished"



@app.route("/init")
def init():
    initTable()
    movieList = db.session.query(Movie).all()
    for temp in movieList:
        print(temp.name, temp.year)    
    return render_template("index.html",movieList=movieList)

@app.route("/home")
def homePage():
    movieList = db.session.query(Movie).all()
    return render_template("index.html",movieList=movieList)

@app.route("/deleteMovie/<id>")
def deleteMovie(id):
    movieToDelete = db.get_or_404(Movie, id)
    db.session.delete(movieToDelete)
    db.session.commit()

    movieList = db.session.query(Movie).all()

    return render_template("index.html",movieList=movieList)

@app.route("/updateMove/<id>")
def updateMovie(id):
    movieToUpdate = db.get_or_404(Movie, id)
    movieToUpdate.year = "2024"
    db.session.commit()

    movieList = db.session.query(Movie).all()

    return render_template("index.html",movieList=movieList)



