from flask_login import UserMixin
from datetime import datetime
from . import db, login_manager


# TODO: implement
@login_manager.user_loader
def load_user(user_id):
    pass

# TODO: implement fields
class User(db.Document, UserMixin):
    username = None
    email = None
    password = None
    profile_pic = None

    # Returns unique string identifying our object
    def get_id(self):
        # TODO: implement
        pass


# TODO: implement fields
class Review(db.Document):
    commenter = None
    content = None
    date = None
    imdb_id = None
    movie_title = None
    #image = db.StringField()
    #Uncomment when other fields are ready for review pictures