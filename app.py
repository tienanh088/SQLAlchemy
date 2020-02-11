from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            student = Students(name=request.form['name'], city=request.form['city'], addr=request.form['add'], pin=request.form['pin'])

            db.session.add(student)
            db.session.commit()
            msg = "Record was successfully added"
        except:
            msg = "Error in insert operation"
        finally:
            return render_template('result.html', msg = msg)

@app.route('/list')
def list():
    return render_template('list.html', students = Students.query.all())

@app.route('/')
def home():
    return render_template('home.html')