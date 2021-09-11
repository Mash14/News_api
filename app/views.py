from app.request import get_sources
from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting sources
    sources = get_sources()
    title = 'Home - News Sources'
    return render_template('index.html', title = title, sources = sources)


@app.route('/source/<source_id>')
def article():
    '''
    View article page that returns the articles page and its data
    '''

    title = 'Articles'
    return render_template('article.html', title = title)