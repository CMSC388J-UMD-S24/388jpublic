from flask import Flask, render_template, request, redirect, url_for
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'f\xb2\xe2\x9a>K(\x82Pc\xc9\x82\xc2P\xce0'

posts = [
    {
        'user': 'elonmusk',
        'text': 'The sun is a thermonuclear explosion fyi'
    },
    {
        'user': 'john',
        'text': 'Excited for school!!!!'
    }
]

@app.route('/')
@app.route('/index')
def index_route():
    return render_template('index.html', posts=posts)

@app.route('/createpost', methods=['GET', 'POST'])
def createpost_route():
    form = CreatePostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            global posts
            posts.append({
                'user': form.user.data,
                'text': form.text.data
            })
            # if you want to redirect to the same route the form is on
            # you can use redirect(request.path)
            return redirect(url_for('index_route'))
    return render_template('createpost_form.html', form=form)

@app.route('/user/<user>')
def user_route(user):
    user_posts = [post for post in posts if post['user'] == user]
    return render_template('user.html', user=user, user_posts=user_posts)


class CreatePostForm(FlaskForm):
    user = StringField('User', validators=[InputRequired(), Length(min=2, max=5)])
    text = StringField('Text', validators=[InputRequired()])
    submit = SubmitField('Submit')

    # validates the text field using a custom validator
    # error will show up in form.text.errors
    # note that we could've just used the Length(min=2, max=10) validator 
    # (which is preferred because it also provides client-side validation via HTML)
    def validate_text(self, text):
        if not (2 <= len(text.data) <= 10):
            raise ValidationError('text should be between 2 and 10 characters')