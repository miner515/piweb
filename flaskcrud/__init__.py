from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

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
        db.session.add(insertUser)
        db.session.commit()

        return redirect(url_for('index'))
@app.route('/delete/<uid>')
def delete(uid):
    delUser=Employee1.query.get(uid)#select * from Employee where userid=3
    db.session.delete(delUser)
    db.session.commit()

    return redirect(url_for('index'))
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
