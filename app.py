from flask import Flask,render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    # return "<p>Hello, World!!!!!</p>"
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
