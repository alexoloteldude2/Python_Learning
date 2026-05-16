from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

prefix = 'sqlite:////'
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'myLoginDB.db')

db.init_app(app)


class User(db.Model):  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键
    name = db.Column(db.String(20))  # 名字
    username = db.Column(db.String(20))  # 用户名
    password_hash = db.Column(db.String(128))  # 密码散列值

    def set_password(self, password):  # 用来设置密码的方法，接受密码作为参数
        self.password_hash = generate_password_hash(password)  # 将生成的密码保持到对应字段

    def validate_password(self, password):  # 用于验证密码的方法，接受密码作为参数
        return check_password_hash(self.password_hash, password)  # 返回布尔值

with app.app_context(): 
    db.create_all()

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/newuser")
def newUser():
    password = generate_password_hash("123")
    user = User(name="qiqi", username="qiqi",password_hash=password)
    db.session.add(user)
    db.session.commit()
    return "New user created"

    
@app.route("/login", methods=['post'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    user = db.session.query(User).filter_by(username = username).first()

    if(user is None) or user.validate_password(password) == False:
        return render_template("loginFail.html")
    else:
        return render_template("loginSuccessful.html")
