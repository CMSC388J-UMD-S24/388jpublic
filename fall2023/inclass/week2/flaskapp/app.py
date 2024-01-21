from flask import Flask, render_template

app = Flask(__name__)

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

@app.route('/user/<user>')
def user_route(user):
    user_posts = [post for post in posts if post['user'] == user]
    return render_template('user.html', user=user, user_posts=user_posts)