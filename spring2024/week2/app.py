from flask import Flask, render_template

app = Flask(__name__)

users = [
    {
        'name': 'anders',
        'text': 'meow'
    },
    {
        'name': 'chuck',
        'text': 'smile :]'
    },
    { 
        'name': 'nikita',
        'text': 'DROP TABLE users;'
    }
]

@app.route('/')
def default():
    return render_template('base.html');

@app.route('/home')
def index_route():
    return render_template('home.html', title='Home', users=users)

@app.route('/about')
def about():
  return 'THIS IS A FUN CLASS :}'

@app.route('/contact/<name>/<name2>')
def contact(name, name2):
  return f'Hello, {name} {name2}'