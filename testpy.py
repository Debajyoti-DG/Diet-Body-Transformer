from flask import Flask
from flask_mail import Mail

testpy = Flask(__name__)

testpy.config['MAIL_SERVER'] = 'smtp.gmail.com'
testpy.config['MAIL_PORT'] = 465
testpy.config['MAIL_USERNAME'] = 'thehecker18@gmail.com'
testpy.config['MAIL_PASSWORD'] = 'btfb kxbx iorc jdik'
testpy.config['MAIL_USE_TLS'] = False
testpy.config['MAIL_USE_SSL'] = True

mail = Mail(testpy)

@testpy.route("/", methods = ['GET', 'POST'])
def index():
    # msg = Message('Hello from the other side !' , sender = ['MAIL_USEERNAME'] , recipients = 'dattaguptadebajyoti@gmail.com')
    # msg.body = "Heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy user !!!!!!!!!"

    mail.send_message('New message from DRS-179', 
                          sender = 'thehecker18@gmail.com', recipients = 'thehecker18@gmail.com', 
                          body = "Hello this is a mail from DRS to test if there is error in authenticaton SMTP. \n If you are reading this then your : " + "\nHeight : 10 cms"  # type: ignore
                          )
    # mail.send(msg)
    return "Message sent"