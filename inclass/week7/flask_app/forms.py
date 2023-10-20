from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.fields import StringField, SubmitField, PasswordField, FileField
from wtforms.validators import ValidationError, InputRequired, Length, Email, EqualTo 
from .models import User

class CreatePostForm(FlaskForm):
    text = StringField('Text', validators=[InputRequired()])
    submit = SubmitField('Submit')

    # validates the text field using a custom validator
    # error will show up in form.text.errors
    # note that we could've just used the Length(min=2, max=15) validator 
    # (which is preferred because it also provides client-side validation via HTML)
    def validate_text(self, text):
        if not (2 <= len(text.data) <= 15):
            raise ValidationError('text should be between 2 and 15 characters')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=10)])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already taken')
    
    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user is not None:
            raise ValidationError('Email already taken') 

class UploadPhotoForm(FlaskForm):
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['png', 'jpg'])
    ])
    submit = SubmitField('Upload')