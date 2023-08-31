from flask import Flask,render_template,request,redirect,url_for,session
import requests
#refer to flask mail documentaion for more info
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import MySQLdb.cursors
import json
import re
import mysql.connector
from flask_cors import CORS


from sqlalchemy import types





local_server= True
with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
CORS(app)


app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail_user'],
    MAIL_PASSWORD = params['gmail_password'],
    SQLALCHEMY_DATABASE_URI = '.db',
    SECRET_KEY = 'FSDFFS2748347ybfjdkFhsfziugcfgtghfxl'
)
mail = Mail(app)

# Database name In my case database name is projectreporting
app.config['MYSQL_DB'] = 'diet_body_transformer'

mysql = MySQL(app)

# cursor = mysql.connection.cursor()


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
    # email = db.Column(db.String(120), unique=True)

    sql_Query = "INSERT INTO `users` ( `name`, `email`, `password`, `age`, `height`, `weight`, `gender`) VALUES ('name', 'email', 'password', 'age', 'height', 'weight', 'gender');"
    
    
    # "INSERT INTO `users` ( `name`, `email`, `password`, `age`, `height`, `weight`, `gender`) VALUES ('Saptarshi', 'saptarshi@gmail.com', 'hello 123', '16', '24', '50', 'male');"

   

    print(sql_Query)




@app.route("/", methods = ['GET', 'POST'])
def home():
    email = ""
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


    response = {'status':'success', 'email':email};
    

    return 'se'

# CORS 

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
    return render_template('barriers.html', params=params_


@app.route("/dashboard", methods = ['GET', 'POST'])
def dashboard():

    print("Hello Dashboard")
    connection = MySQLdb.connect(host='localhost',database='diet_body_transformer',user='root',password='')
    sql_select_Query = "select * from users"
    print("next")

    cursor = connection.cursor()
    cursor.execute(sql_select_Query)


    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Password  = ", row[2])
        print("Created At  = ", row[3], "\n")
    

    # cursor = connection.cursor()

    return render_template('dashboard.html', params=params)
   






# @app.route("/login", methods = ['GET','POST'])
# def login():
#     if request.method == 'GET':
#         return "login via the login form"
#     if request.method == 'POST':
#         id = request.form['id']
#         name = request.form['name']
#         email = request.form['email']
#         age = request.form['email']
#         height = request.form['height']
#         weight = request.form['weight']
#         gender = request.form['gender']
#         password = request.form['password']
#         created_at = request.form['created_at']

#         cursor = mysql.connection.cursor()
#         cursor.execute(users (id, name, email, age, height, weight, gender, password))

#         cursor.execute(users VALUES(%d, %s, %s, %s, %s, %s, %s, %s), (id, name, email, age, height, weight, gender, password))

#         mysql.connection.commit()
#         cursor.close()

#     return render_template('login.html', params=params)



