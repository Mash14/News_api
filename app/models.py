class Source:
    '''
    Source class to define Source Objects
    '''


    def __init__(self,id,name,description):
        """
        __init__method that helps to define properties of our objects
        
        Args:
            id: New source id
            name: New source name
            description: New source description
        """
        
        self.id = id
        self.name = name
        self.description = description
    

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
        
