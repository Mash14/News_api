class Article:
    '''
    Class that defines Article Objects
    '''
    def __init__(self,source,title,urlToImage,description,urlToArticle,publishedAt):
        '''
        define properties of an article
        '''
        self.source = source
        self.title = title
        self.urlToImage = urlToImage
        self.description = description
        self.urlToArticle = urlToArticle
        self.publishedAt = publishedAt
        

    