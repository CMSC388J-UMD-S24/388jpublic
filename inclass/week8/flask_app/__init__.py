from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

def error404(error):
    return render_template('404.html'), 404

db = MongoEngine()
login_manager = LoginManager()
bcrypt = Bcrypt()

# import blueprints after initializing variables to prevent partially-initialized circular dependency issue
from .main.routes import main_blueprint
from .posts.routes import posts_blueprint
from .users.routes import users_blueprint

def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_pyfile("config.py", silent=True)
    if test_config is not None:
        app.config.update(test_config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    # if the user is not logged in for a route that requires it, redirect to login_route
    login_manager.login_view = 'users.login_route'

    app.register_blueprint(main_blueprint)
    app.register_blueprint(posts_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_error_handler(404, error404)

    return app