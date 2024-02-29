from flask import Flask, render_template, request, redirect, url_for
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_wtf import FlaskForm
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['SECRET_KEY'] = b'f\xb2\xe2\x9a>K(\x82Pc\xc9\x82\xc2P\xce0'
app.config['MONGO_URI'] = 'mongodb+srv://cmsc388j:<password>@cluster0.lograwo.mongodb.net/week4_db?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index_route():
    posts = list(mongo.db.posts.find())
    return render_template('index.html', posts=posts)

@app.route('/createpost', methods=['GET', 'POST'])
def createpost_route():
    form = CreatePostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_post = {
                'user': form.user.data,
                'text': form.text.data
            }
            mongo.db.posts.insert_one(new_post)
            # if you want to redirect to the same route the form is on
            # you can use redirect(request.path)
            return redirect(url_for('index_route'))
    return render_template('createpost_form.html', form=form)

@app.route('/user/<user>')
def user_route(user):
    # should convert to list because the return type is a MongoDB Cursor
    user_posts = list(mongo.db.posts.find({'user': {'$eq': user}}))
    return render_template('user.html', user=user, user_posts=user_posts)

@app.route('/post/<id>')
def post_route(id):
    post = mongo.db.posts.find_one({'_id': {'$eq': ObjectId(id)}})
    return render_template('post.html', post=post)

class CreatePostForm(FlaskForm):
    user = StringField('User', validators=[InputRequired(), Length(min=2, max=10)])
    text = StringField('Text', validators=[InputRequired()])
    submit = SubmitField('Submit')

    # validates the text field using a custom validator
    # error will show up in form.text.errors
    # note that we could've just used the Length(min=2, max=15) validator 
    # (which is preferred because it also provides client-side validation via HTML)
    def validate_text(self, text):
        if not (2 <= len(text.data) <= 15):
            raise ValidationError('text should be between 2 and 15 characters')