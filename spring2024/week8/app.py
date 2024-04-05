from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def index_route():
    return render_template('index.html')

# api route for fetch example
@app.route("/rand")
def hello():
    return str(random.randint(0, 100))
