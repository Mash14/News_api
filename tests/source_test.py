import unittest
from app.models import Source


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('news_tech', 'News Technology', 'The fastest and most reliable  news source on technology')


    def test_init(self):
        '''
        Method to test if the object is being initialized properly
        '''
        self.assertEqual(self.new_source.id,'news_tech')
        self.assertEqual(self.new_source.name, 'News Technology')
        self.assertEqual(self.new_source.description,'The fastest and most reliable  news source on technology')

        
    def test_instance(self):
        '''
        Method to test if the object is being initialized
        '''
        self.assertTrue(isinstance(self.new_source,Source))


if __name__ == '__main__':
    unittest.main()