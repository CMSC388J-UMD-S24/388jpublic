from . import db, login_manager
from flask_login import UserMixin 

class Post(db.Document):
    username = db.StringField(required=True)
    text = db.StringField(required=True)

class User(db.Document, UserMixin):
    email = db.EmailField(unique=True, required=True)
    username = db.StringField(unique=True, required=True)
    password = db.StringField(required=True)
    profile_pic = db.ImageField()

    def get_id(self):
        return self.username

@login_manager.user_loader
def load_user(user_id):
    return User.objects(username=user_id).first()