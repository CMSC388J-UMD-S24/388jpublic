# P3: Movie Ratings Database

**Assigned**: February 17th

**Deadline**: March 1st, 11:59 PM Eastern

**Late deadline**: March 3rd 11:59 PM Eastern

## Description

You will be constructing the forms and database-accessing parts of a movie rating
website so that users can search for movies and leave reviews for the world to see.

You *may* add more fields to the models if you want. You just have to include
the required fields, as detailed below.

**Note:** On the slides, we taught you to check if the `request.method == 'POST'` and then
to check if the form can be validated with `if form.validate()`. However, using this
approach will not allow the error messages to show up.

To get the error messages to show up, use `if form.validate_on_submit()` to check
that the form was submitted and to validate it in one step. This allows you to
display any errors that are thrown by the custom or built-in validators 
from your forms. 

**Side Note:** The OMDB API returns movies *and* TV shows. You don't have to worry
about distinguishing between types of media. Just to alleviate any concerns. :)

## Setup

Activate your virtual environment and use
`pip3 install -r requirements.txt` or
`pip3 install Flask Flask-WTF Flask-PyMongo python-dotenv requests`.

The setup involves getting an API key and installing the necessary packages. 

### Setup (OMDb):
1. Navigate to The Open Movie Database website -- http://www.omdbapi.com/
   ![alt text](images/omdb_home.png "The OMDb homepage")
2. Request an API key and navigate to the email you used to sign up with OMDb, and
   verify your API key.
   ![alt text](images/request_key.png "Request an API Key")
3. Using the API key you received in your email, fill in the `OMDB_API_KEY` variable at the top `app.py`.

## Project

This is the `p3/` directory structure

![directory structure](images/dir_structure.png)

**Only modify:** `app.py` and `forms.py`. 

There's a README, this document, containing your instructions to complete the project. The
`images/` folder consists of images used in the README, so it is not anything
you have to worry about while implementing your project. `requirements.txt` contains
all of the packages you should have installed (with `pip3 install -r requirements.txt`).

The `flask_app/` directory contains `app.py`, where all of your view functions and app setup
are located, `forms.py`, containing the two forms you will have to implement, `model.py`,
which provides two classes: `Movie` and `MovieClient`, which is how you'll interact with the
OMDb API, a `static/` folder consisting of custom CSS (don't worry about this), and
`templates/`, consisting of all templates you'll use for this project. 

First, we'll explain `model.py`:
- `model.py` consists of two classes. One is a `Movie` class, the other `MovieClient`.
- The `MovieClient` class is instansiated with an API key (don't worry about this
  once you've set your environment variable), and it has two methods for you to use:
  - `search()` takes a `search_string` that the user entered into the search box
    on the index page, and it returns a `list` of `Movie` objects. If an error
    occurs, a `ValueError` will be raised with the error message.
  - `retrieve_movie_by_id()` takes an `imdb_id` and returns a `Movie` object with more data
    on that particular movie. If an error occurs, a `ValueError` will be raised
    with the error message.
- The `Movie` class consists of up to 10 attributes. If a detailed movie request is made, then
  it contains all 10. Otherwise, if just being searched for using `MovieClient.search()`, it will
  have the basic 5 attributes (title, year, imdb_id, type, poster_url).


Here's what you need to do for this project, file by file:
1. `app.py`:
   - Set the api key, database uri, secret keys, so that Mongo works and the CSRF tokens
      can be generated. 
   - Use **MongoDB** to store the reviews that have been submitted. Not using MongoDB
     (if you use SQLite or some other database, or the `session` object), will result in a 0.
   - In `query_results(query)`, you'll need to use the `MovieClient` class to search 
     movies matching `query`. If an error is encountered,
     the error message should be displayed, and no query results. If the search is
     successful (list of `Movie`s returned), then display those Movies (the template
     is taken care of)
   - In `movie_detail(movie_id)`, use the `MovieClient` class to get a detailed
     view of the movie identified by `movie_id`. If it has a retrieval error, 
     show the error message. If no error, then create the MovieReviewForm. Then 
     if `validate_on_submit()` is true, store the movie review with 
     **4 parameters: `imdb_id`, `commenter`, `content`, and `date`**. You **MUST** store all reviews in a MongoDB collection named **`reviews`**. 
     After successful storing, redirect so the user can see their published review. 
   - Additionally in `movie_detail(movie_id)`, all of the reviews that users have submitted
     for that movie must be displayed. The template takes care of displaying, you have to
     provide the data.
   - **Note:** There is a `current_time()` function at the bottom of `app.py` that returns
     the current date and time as a neatly-formatted string.
   - **Second note:** To determine what parameters to pass in to templates, inspect the templates.
1. `forms.py`:
   - Create the two forms `SearchForm` and `MovieReviewForm`.
   - `SearchForm` has a text-box for entering a query, and a submit button. Check out
     the `index()` view function and the `index.html` template
     to see what the form elements should be named.
     The query should be at least 1 character long, but no more than 30. **All fields are required.** You should use validators provided by Flask-WTF.
   - `MovieReviewForm` has a text-box for a commenter to enter their name or an alias, and
     a larger text area for a commenter to type out the full content of their post, along
     with a button for submission. A name should be at least 1 character long, no more than 50, and the content of a comment
     should be at least 1 character, but no more than 500. **All fields are required.** You should use validators provided by Flask-WTF.
     The names for these fields can be determined by looking at the `movie_detail.html` template.

**Hint for MovieReviewForm:** You should use a field that allows multi-line input.
Refer to https://wtforms.readthedocs.io/en/2.3.x/validators/ for a list of built-in validators.

## Testing

Please make sure you haven't modified the template files.

When your current directory is `flask_app/`, you can simply run the command `flask run`
in your terminal or command line to see your website.

Make sure the index page shows up, and that you can enter queries for movies in the form.
If any errors occur while querying, the error message should be shown on the query page.
If no errors occurred, we should see a list of movie posters and titles. For exmaple, searching
`guardians` yields 113 results. Then clicking on one of these titles should take us to
the detail page. Here we see lots of extra information on the movie in a card at the top,
and we should see all the reviews users left below that, and then the form for submitting
reviews below that. If the movie detail retrieval fails, the error message for the failure should 
be displayed, without any of the reviews or the form being displayed.

The navbar header should take you back to the main page, where you can search for more movies.

## Submissions

Assure that you've tried out all the different things that could go wrong and that they
are behaving appropriately (and the things that are supposed to work, still do).

*Before zipping, delete the `venv/` directory from `p3/` if you created one.\
**The directory, along with its contents, should be zipped, not the contents of the directory.**
In other words, when we unzip your file, we should see the `p3/` directory. If you
have any questions on how to submit, please contact us.

If you don't submit according to the instructions above, you may lose **up to 25%** of your
score on this project.

After zipping, submit the zip file to the appropriate Gradescope page.

## Grading

If you don't use MongoDB, you will get a 0 on this project.

Your project will be graded on (1) correctness and (2) robustness.
Here are the **correctness** requirements:

**Correctness**:

| Requirement                                        | Points |
|----------------------------------------------------|--------|
| Secret Key Set                                     | 5      |
| Search form rendered with input validators         | 10     |
| Search form input validator errors shown on page   | 5      |
| Query results show up after submitting search form | 15     |
| Review form rendered with input validators         | 10     |
| Review form input validator errors shown on page   | 5      |
| Review form has multi-line input for review        | 5      |
| Reviews are shown after submitting review form     | 10     |
| Review are shown per movie (unique per movie)      | 15     |
| Reviews are inserted into MongoDB                  | 15     |
| Reviews are read from MongoDB                      | 15     |

There's a total of 110 points.

**Robustness:**

Refer to the syllabus for the robustness requirement for all projects.
The syllabus has been updated recently with this information, since
it will be common to all projects.
