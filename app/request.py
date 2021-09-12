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
    get_sources_url = 'https://newsapi.org/v2/sources?apiKey={}'.format(api_key)

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


def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_respose = json.loads(get_articles_data)

        article_object = None

        if get_articles_respose:
            source = get_articles_respose.get('source')
            title = get_articles_respose.get('title')
            urlToImage = get_articles_respose.get('urlToImage')
            description = get_articles_respose.get('description')
            urlToArticle = get_articles_respose.get('url')
            publishedAt = get_articles_respose.get('publishedAt')

            article_object = Article(source,title,urlToImage,description,urlToArticle,publishedAt)

    return article_object


