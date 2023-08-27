from flask import Flask,render_template,request,redirect,url_for,session
import requests
#refer to flask mail documentaion for more info
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import MySQLdb.cursors
import json
import re







local_server= True
with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail_user'],
    MAIL_PASSWORD = params['gmail_password'],
    SQLALCHEMY_DATABASE_URI = 'mysql:///users.db',
    SECRET_KEY = 'FSDFFS2748347ybfjdkFhsfziugcfgtghfxl'
)
mail = Mail(app)


















#code for connection
#MySQL Hostname
# app.config['MYSQL_HOST'] = 'localhost'
#MySQL username
# app.config['MYSQL_USER'] = 'root'
#MySQL password here in my case password is null so i left empty
# app.config['MYSQL_PASSWORD'] = ''
#Database name In my case database name is projectreporting
app.config['MYSQL_DB'] = ''

mysql = MySQL(app)



# @app.route('/')
# @app.route('/dashboard',methods=['GET','POST'])
# def projectlist():


    #placed in dashboard

    # #creating variable for connection
    # cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # #executing query
    # cursor.execute("select * from pro_reg")
    # #fetching all records from database
    # data=cursor.fetchall()

























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


@app.route("/roadmap")
def roadmap():
    # return "<p>Hello, World!!!!!</p>"
    return render_template('roadmap.html', params=params)

@app.route("/contact")
def contact():
    # return "<p>Hello, World!!!!!</p>"
    return render_template('contact.html', params=params)

@app.route("/barriers")
def barriers():
    # return "<p>Hello, World!!!!!</p>"
    return render_template('barriers.html', params=params)

@app.route("/dashboard", methods = ['GET', 'POST'])
def dashboard():
    # return "<p>Hello, World!!!!!</p>"


    # # At night

    # #creating variable for connection
    # cursor=mysql.connect.cursor()
    # #executing query
    # cursor.execute("select * from pro_reg")
    # #fetching all records from database
    # data=cursor.fetchall()

    return render_template('dashboard.html', params=params)
