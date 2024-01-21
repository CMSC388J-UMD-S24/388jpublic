# 3rd-party packages
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

# stdlib
import os
from datetime import datetime

# local
from flask_app.forms import SearchForm, MovieReviewForm
from flask_app.model import MovieClient

# don't change the name
app = Flask(__name__)

# TODO: you should fill out these with the appropriate values
app.config['MONGO_URI'] = '' 
app.config['SECRET_KEY'] = ''
OMDB_API_KEY = '' 

# DO NOT REMOVE OR MODIFY THESE 4 LINES (required for autograder to work)
if os.getenv('MONGO_URI'):
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
if os.getenv('OMDB_API_KEY'):
    OMDB_API_KEY = os.getenv('OMDB_API_KEY')

app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)

# don't change the name
mongo = PyMongo(app)

# don't change the name 
movie_client = MovieClient(OMDB_API_KEY)

# --- Do not modify this function ---
@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()

    if form.validate_on_submit():
        return redirect(url_for('query_results', query=form.search_query.data))

    return render_template('index.html', form=form)

@app.route('/search-results/<query>', methods=['GET'])
def query_results(query):
    return 'Query'

@app.route('/movies/<movie_id>', methods=['GET', 'POST'])
def movie_detail(movie_id):
    return 'movie_detail'

# Not a view function, used for creating a string for the current time.
def current_time() -> str:
    return datetime.now().strftime('%B %d, %Y at %H:%M:%S')