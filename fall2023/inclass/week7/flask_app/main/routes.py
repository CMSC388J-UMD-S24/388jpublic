from flask import Blueprint, render_template
from flask_login import current_user

from ..models import Post

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
@main_blueprint.route('/index')
def index_route():
    posts = list(Post.objects())
    return render_template('index.html', posts=posts, current_user=current_user)

