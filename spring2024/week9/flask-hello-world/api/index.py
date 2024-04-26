from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

# api route for fetch example
@app.route("/rand")
def hello():
    return str(random.randint(0, 100))