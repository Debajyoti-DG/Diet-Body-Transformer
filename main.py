from flask import Flask, request, session, make_response,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
from flask_cors import CORS
from flask_session import Session

app = Flask(__name__)
CORS(app)

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail_user'],
    MAIL_PASSWORD = params['gmail_password'],
    SQLALCHEMY_DATABASE_URI = 'diet_body_transformer',
    SECRET_KEY = 'FSDFFS2748347ybfjdkFhsfziugcfgtghfxl'
)
mail = Mail(app)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'

# Configuration for SQLAlchemy 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/diet_body_transformer'
app.config['SECRET_KEY'] = 'hdWEFUWFW$634W32'

Session(app)
db = SQLAlchemy(app)




# print('My session: ',session.get('')) # null

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False)
    email = db.Column(db.String(70), unique=True)
    password = db.Column(db.String(64), unique=False)
    age = db.Column(db.String(3), unique=False)
    height = db.Column(db.String(6), unique=False)
    weight = db.Column(db.String(6), unique=False)
    gender = db.Column(db.String(12), unique=False)

class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gain_weight = db.Column(db.String(20), primary_key=False)
    lose_weight = db.Column(db.String(20), primary_key=False)
    build_muscle = db.Column(db.String(20), primary_key=False)
    get_fit = db.Column(db.String(20), primary_key=False)
    be_flexy = db.Column(db.String(20), primary_key=False)
    email = db.Column(db.String(70), primary_key=False)
    

@app.route("/", methods=['GET', 'POST'])
def home():
    email = ""
    response = make_response() 

    if request.method == 'POST':
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        height = request.form.get('height')
        weight = request.form.get('weight')
        age = request.form.get('age')
        gender = request.form.get('gender')
        password_user = request.form.get('password')

        # Create a User instance and commit to the database
        entry = User(name=name, email=email, height=height, weight=weight, age=age, gender=gender, password=password_user)
        db.session.add(entry)
        db.session.commit()

        mail.send_message('New message from ' + params['name'], 
                          sender = email, recipients = [params['gmail_user']], 
                          body = "Hello this is a mail from DRS . \n If you are reading this then your : " + "\nEmail : " + email + "\n. " + "We are glad that you decided to be a part of our community. We will launch a more user friendly version soon. This is where we will notify you about further updates. Stay tuned !" # type: ignore
                          )


        response.set_cookie('email',request.form.get('email'))

        response_json = {'status': 'success', 'email': email}
        response.set_data(json.dumps(response_json))
    
    elif request.method == "GET":
        response.status_code = 404
    
    return render_template('index.html', params = params)




@app.route("/getUser", methods=['GET', 'POST'])
def session_route():

    response = {}

    email = request.cookies.get('email')
    user = User.query.filter_by(email=email).first()


    if not user:
        # the email doesnt exist
        
        response['status'] = 'failed'
        response['message'] = 'email does not exist'
    else:
        # the email exists
        print (type(user))
        print (user.name)
        response['status'] = 'success'
        response['message'] = 'email exists'
        response['name'] = user.name
        response['age'] = user.age
        response['height'] = user.height
        response['weight'] = user.weight
        response['gender'] = user.gender
        response['email'] = user.email

    return json.dumps(response)
    


@app.route("/choice", methods = ['GET','POST'])
def choice_user():
    
    response_json = {

    } 
    email = request.cookies.get('email')

    if request.method == 'POST':
        # Extract form data
        
        gain_weight = request.form.get('gain_weight')
        lose_weight = request.form.get('lose_weight')
        build_muscle = request.form.get('build_muscle')
        get_fit = request.form.get('get_fit')
        be_flexy = request.form.get('be_flexy')
        

        # Create a User choice instance and commit to the database
        entry = Choice(gain_weight=gain_weight, lose_weight=lose_weight, build_muscle=build_muscle, get_fit=get_fit, be_flexy=be_flexy, email= email)
        db.session.add(entry)
        db.session.commit()

        response_json['status'] = 'success'
        response_json['message'] = 'email exists'
    
    return json.dumps(response_json)

@app.route("/barriers", methods = ['GET','POST'])
def barriers():
    return render_template('barriers.html',params=params)
@app.route("/dashboard", methods = ['GET','POST'])
def dashboard():
    return render_template('dashboard.html',params=params)