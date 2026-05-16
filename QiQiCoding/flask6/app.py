from flask import Flask,render_template, request
app=Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('formPage.html')

@app.route("/handleForm", methods = ['POST'])
def handForm():
    name = request.form.get("name")
    occupation = request.form.get("occupation")

    return render_template('display.html',name=name,occupation=occupation)


