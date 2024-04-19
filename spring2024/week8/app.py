from flask import Flask, render_template
import random
import time
app = Flask(__name__)

@app.route('/')
def index_route():
    return render_template('index.html')

@app.route('/week13')
def week_route():
    return render_template('week13.html')

# api route for fetch example
@app.route("/rand")
def hello():
    time.sleep(2);
    return str(random.randint(0, 100))
