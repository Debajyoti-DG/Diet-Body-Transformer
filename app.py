from flask import Flask,render_template,request
import requests
#refer to flask mail documentaion for more info
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
import json

local_server= True
with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail_user'],
    MAIL_PASSWORD = params['gmail_password']
)
mail = Mail(app)

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

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
        mail.send_message('New message from ' + params['name'], 
                          sender = email, recipients = [params['gmail_user']], 
                          body = "Hello this is a mail from DRS to test if there is error in authenticaton SMTP. \n If you are reading this then your : " + "\nHeight : " + height + " cms"  # type: ignore
                          )

    return render_template('index.html', params=params)


# @app.route("/")
# def home():
#     # return "<p>Hello, World!!!!!</p>"
#     return render_template('style.css')

@app.route("/roadmap")
def roadmap():
    # return "<p>Hello, World!!!!!</p>"
    return render_template('roadmap.html', params=params)

@app.route("/contact")
def contact():
    # return "<p>Hello, World!!!!!</p>"
    return render_template('contact.html', params=params)
