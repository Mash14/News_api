from app import app
import urllib.request,json
from .models import source,article

Source = source.Source
Article = article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news api base url
base_url = app.config['NEWS_API_BASE_URL']


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = 'https://newsapi.org/v2/sources?apiKey={}'.formart(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            source_results = process_sources(sources_results_list)

        
    return source_results


def process_sources(source_list):
    '''
    Function that processes the sources results and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain the source details

    Returns:
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')

        source_object = Source(id,name,description)

        source_results.append(source_object)

    return source_results


def get_articles():
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_respose = json.loads(get_articles_data)

        article_results = None

        if get_articles_respose['articles']:
            articles_results_list = get_articles_respose['articles']
            article_results = process_articles(articles_results_list)

    return article_results


def process_articles(article_list):
    '''
    Function that processes the articles results and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain the articles details

    Returns:
        articles_results: A list of articles objects
    '''
    article_results = []

    for article_item in article_list:
        source = article_item.get('source')
        title = article_item.get('title')
        urlToImage = article_item.get('urlToImage')
        description = article_item.get('description')
        urlToArticle = article_item.get('url')
        publishedAt = article_item.get('publishedAt')

        article_object = Article(source,title,urlToImage,description,urlToArticle,publishedAt)

        article_results.append(article_object)

    return article_results
