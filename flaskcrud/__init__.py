<<<<<<< HEAD
=======
# -*- coding: utf-8 -*-
>>>>>>> 1b5a790aa395cc5dc141bf3b66ff3ee8523cee06
from gtts import gTTS
from playsound import playsound
from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

<<<<<<< HEAD
app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shindalsoo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(200))
    tel = db.Column(db.String(50))

    def __init__(self, username, email, tel):
        self.username = username
        self.email = email
        self.tel = tel

@app.route('/')
def index():
    all_data = Employee.query.order_by(Employee.userid.desc()).all() # select * from employee
    return render_template("index.html", employees=all_data)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        tel = request.form['tel']

        insertUser = Employee(username,email,tel)
=======
app=Flask(__name__)
app.secret_key="Secret key"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///junho.db'
#app.config['SQLALCHEMY_DATABASE_URI']='mysql://id@비밀번호'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Employee1(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(100))
    jicwi=db.Column(db.String(100))
    email=db.Column(db.String(100))
    tel=db.Column(db.String(100))
    
    def __init__(self, username,jicwi, email, tel):
        self.username=username
        self.jicwi = jicwi
        self.email=email
        self.tel=tel
@app.route('/')
def index():
    all_data=Employee1.query.order_by(Employee1.id.desc()).all() #select * from employee
    return render_template("index.html",employee1=all_data)
@app.route('/insert', methods=['POST'])
def insert():
    if request.method =='POST':
        username=request.form['username']
        jicwi = request.form['jicwi']
        email=request.form['email']
        tel=request.form['tel']

        insertUser=Employee1(username,jicwi,email, tel)
>>>>>>> 1b5a790aa395cc5dc141bf3b66ff3ee8523cee06
        db.session.add(insertUser)
        db.session.commit()

        return redirect(url_for('index'))
<<<<<<< HEAD

@app.route('/delete/<uid>')
def delete(uid):
    delUser = Employee.query.get(uid) # select * from Employee where userid=3
=======
@app.route('/delete/<uid>')
def delete(uid):
    delUser=Employee1.query.get(uid)#select * from Employee where userid=3
>>>>>>> 1b5a790aa395cc5dc141bf3b66ff3ee8523cee06
    db.session.delete(delUser)
    db.session.commit()

    return redirect(url_for('index'))
<<<<<<< HEAD

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        updateUser = Employee.query.get(request.form.get('userid'))
        updateUser.username = request.form['username']
        updateUser.email = request.form['email']
        updateUser.tel = request.form['tel']
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/search', methods=['POST'])
def search():
    txtsearch = request.form['txtsearch']
    searchUser = Employee.query.filter(Employee.username.contains(txtsearch))
    return render_template("index.html", employees=searchUser, txtsearch=txtsearch)

@app.route('/playmp3')
def playmp3():
    text = "오늘은, 2020년 8월 20일입니다. 고양이가 소리를 내려고합니다. 우리모두 스마트고양이를 응원합시다~~람쥐"
    filename = "hellosmartcat.mp3"
    tts = gTTS(text=text, lang='ko')
    tts.save(filename)
    playsound(filename)

    return "고양이가 소리를 냈습니다."
=======
@app.route('/update',methods=['POST'])
def update():
    updateUser=Employee1.query.get(request.form.get('id'))
    updateUser.username=request.form['username']
    updateUser.jicwi=request.form['jicwi']
    updateUser.email=request.form['email']
    updateUser.tel=request.form['tel']
    db.session.commit()

    return redirect(url_for('index'))
@app.route('/search' ,methods=['POST'])
def search():
    textsearch=request.form['textsearch']
    searchUser=Employee1.query.filter(Employee1.username.contains(textsearch))
    return render_template("index.html",employee1=searchUser, textsearch=textsearch)
@app.route('/playmp3')
def playmp3():
    text="고양이가 소리냄. 스마트고양이 응원"
    filename="hi.mp3"
    tts=gTTS(text=text, lang='ko')
    tts.save(filename)
    playsound(filename)
    return "소리냄."
>>>>>>> 1b5a790aa395cc5dc141bf3b66ff3ee8523cee06
