from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.utils import secure_filename
import io
import base64

from ..models import User, Post
from ..forms import RegistrationForm, LoginForm, UploadPhotoForm
from .. import bcrypt

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/user/<username>')
def user_route(username):
    # should convert to list because the return type is a MongoDB Cursor
    user_posts = list(Post.objects(username=username))
    user = User.objects(username=username).first()
    profile_pic_bytes = io.BytesIO(user.profile_pic.read())
    profile_pic_base64 = base64.b64encode(profile_pic_bytes.getvalue()).decode()
    return render_template('user.html', username=username, user_posts=user_posts, profile_pic_base64=profile_pic_base64)

@users_blueprint.route('/register', methods=['GET', 'POST'])
def register_route():
    if current_user.is_authenticated:
        return redirect(url_for('main.index_route'))

    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            user.save()
            return redirect(url_for('users.login_route'))
    return render_template('register.html', form=form)

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login_route():
    if current_user.is_authenticated:
        return redirect(url_for('main.index_route'))

    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.objects(username=form.username.data).first()

            if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('users.user_route', username=user.username))
            else:
                flash("Failed to log in!")
    return render_template('login.html', form=form)

@users_blueprint.route('/logout')
def logout_route():
    logout_user()
    return redirect(url_for('main.index_route'))

@users_blueprint.route('/uploadphoto', methods=['GET', 'POST'])
@login_required
def uploadphoto_route():
    form = UploadPhotoForm()
    if form.validate_on_submit():
        image = form.photo.data
        filename = secure_filename(image.filename)
        content_type = f'images/{filename[-3:]}'

        if current_user.profile_pic.get() is None:
            # user doesn't have a profile picture => add one
            current_user.profile_pic.put(image.stream, content_type=content_type)
        else:
            # user has a profile picture => replace it
            current_user.profile_pic.replace(image.stream, content_type=content_type)
        current_user.save()
        return redirect(url_for('users.user_route', username=current_user.username))
    return render_template('uploadphoto.html', form=form)