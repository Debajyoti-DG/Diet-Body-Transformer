from flask import Flask,render_template,request
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/diet_body_transformer'
db = SQLAlchemy(app)

class users(db.Model):

    '''
    id name height weight age gender email password
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False)
    email = db.Column(db.String(70), unique=True)
    password = db.Column(db.String(64), unique=True)
    age = db.Column(db.String(3), unique=False)
    height = db.Column(db.String(6), unique=False)
    weight = db.Column(db.String(6), unique=False)
    gender = db.Column(db.String(12), unique=False)
    email = db.Column(db.String(120), unique=True)


@app.route("/", methods = ['GET', 'POST'])
def home():
    if (request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        height = request.form.get('height')
        weight = request.form.get('weight')
        age = request.form.get('age')
        gender = request.form.get('gender')
        password_user = request.form.get('password')

        entry = users(name=name, email=email, height=height, weight=weight, age=age, gender=gender, password=password_user)
        db.session.add(entry)
        db.session.commit()

    return render_template('index.html')


# @app.route("/")
# def home():
#     # return "<p>Hello, World!!!!!</p>"
#     return render_template('style.css')

@app.route("/roadmap")
def roadmap():
    # return "<p>Hello, World!!!!!</p>"
    return render_template('roadmap.html')

@app.route("/contact")
def contact():
    # return "<p>Hello, World!!!!!</p>"
    return render_template('contact.html')
