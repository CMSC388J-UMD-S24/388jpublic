from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from bson import ObjectId

from ..forms import CreatePostForm
from ..models import Post

posts_blueprint = Blueprint('posts', __name__)

@posts_blueprint.route('/createpost', methods=['GET', 'POST'])
@login_required
def createpost_route():
    form = CreatePostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_post = Post(username=current_user.username, text=form.text.data)
            new_post.save()
            # if you want to redirect to the same route the form is on
            # you can use redirect(request.path)
            return redirect(url_for('main.index_route'))
    return render_template('createpost_form.html', form=form)


@posts_blueprint.route('/post/<id>')
def post_route(id):
    post = Post.objects(pk=ObjectId(id)).first()
    return render_template('post.html', post=post)