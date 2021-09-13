import urllib.request,json
from .models import Source, Article


# Getting api key
api_key = None

# Getting the news api base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = 'https://newsapi.org/v1/sources?'

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
    """
    Function that gets the json response for our url request
    """
    #
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=41f776ca676c42af98145d016eda7056'.format(id)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
        articles_results = None
        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)
    return articles_results


def process_articles(articles_list):
    """
    A function that processes the news result and transform them to a list of objects
    
    Args:
        articles_list: A list of dictionary that returns news details
    
    returns:
         articles_results: A list of news objects
    """
    articles_results = []
    for articles_item in articles_list:
       source = articles_item.get('source') 
       title =  articles_item.get('title')      
       description =  articles_item.get('description')
       urlToArticle =  articles_item.get('url')
       urlToImage =  articles_item.get('urlToImage')
       publishedAt =  articles_item.get('publishedAt')
       
       if urlToImage:
            articles_object = Article(source, title, urlToImage, description, urlToArticle, publishedAt )
            articles_results.append(articles_object)
    
    return  articles_results




