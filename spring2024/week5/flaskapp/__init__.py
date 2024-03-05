from flask import Flask 
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = b'f\xb2\xe2\x9a>K(\x82Pc\xc9\x82\xc2P\xce0'
app.config['MONGODB_SETTINGS'] = {
    'db': 'week5_db',
    'host': 'mongodb+srv://cmsc388j:<password>@cluster0.23mylkm.mongodb.net/week5_db?retryWrites=true&w=majority'
}

db = MongoEngine(app)
login_manager = LoginManager(app)
# if the user is not logged in for a route that requires it, redirect to login_route
login_manager.login_view = 'login_route'
bcrypt = Bcrypt(app)