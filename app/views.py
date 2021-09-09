from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    return render_template('index.html')


@app.route('/articles')
def article():
    '''
    View article page that returns the articles page and its data
    '''

    return render_template('article.html')