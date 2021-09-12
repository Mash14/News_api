from ..request import get_sources,get_articles
from flask import render_template
from . import main


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting sources
    sources = get_sources()
    title = 'Home - News Sources'
    return render_template('index.html', title = title, sources = sources)


@main.route('/source/<id>')
def source(id):
    '''
    View article page that returns the articles page and its data
    '''
    articles = get_articles(id)
    title = f'{id}'
    return render_template('source.html', title = title, articles = articles)