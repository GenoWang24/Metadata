import unittest
import arxiv_functions

# you may not need to use the types, but we have imported them all for you
from constants import (ID, TITLE, CREATED, MODIFIED, AUTHORS, ABSTRACT, END, 
                       NameType, ArticleValueType, ArticleType, ArxivType)


# You can use this sample dictionary in your tests, if you choose
# You can also create your own sample dictionaries 
TEST_ARXIV = {
    '031': {
        ID: '031',
        TITLE: 'Calculus is the Best Course Ever',
        CREATED: '',
        MODIFIED: '2021-09-02',
        AUTHORS: [('Breuss', 'Nataliya')],
        ABSTRACT: 'We discuss the reasons why Calculus is the best course.'},
    '067': {
        ID: '067',
        TITLE: 'Discrete Mathematics is the Best Course Ever',
        CREATED: '2021-09-02',
        MODIFIED: '2021-10-01',
        AUTHORS: [('Pancer', 'Richard'), ('Bretscher', 'Anna')],
        ABSTRACT: ('We explain why Discrete Mathematics is the best ' +
                   'course of all times.')},
    '827': {
        ID: '827',
        TITLE: 'University of Toronto is the Best University',
        CREATED: '2021-08-20',
        MODIFIED: '2021-10-02',
        AUTHORS: [('Ponce', 'Marcelo'), ('Bretscher', 'Anna'), 
                  ('Tafliovich', 'Anya Y.')],
        ABSTRACT: 'We show a formal proof that the University of\n' +
        'Toronto is the best university.'},
    '008': {
        ID: '008',
        TITLE: 'Intro to CS is the Best Course Ever',
        CREATED: '2021-09-01',
        MODIFIED: '',
        AUTHORS: [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')],
        ABSTRACT: 'We present clear evidence that Introduction to\n' + \
        'Computer Science is the best course.'},    
    '042': {
        ID: '042',
        TITLE: '',
        CREATED: '2021-05-04',
        MODIFIED: '2021-05-05',
        AUTHORS: [],
        ABSTRACT: 'This is a strange article with no title\n' + \
        'and no authors.\n\nIt also has a blank line in its abstract!'}
}


class TestContainsKeyword(unittest.TestCase):
    """Test cases for function arxiv_functions.contains_keyword
    """
    
    def test_one_match(self) -> None:
        """Test contains_keyword with the keyword appearing in both the title
        and abstract of one article.
        """
        actual = arxiv_functions.contains_keyword(TEST_ARXIV, 'Toronto')
        expected = ['827']
        self.assertEqual(actual, expected)
    
    def test_no_match(self) -> None:
        """Test contains_keyword with the keyword not appearing in either
        the title or abstract of one article.
        """
        actual = arxiv_functions.contains_keyword(TEST_ARXIV, 'Geno')
        expected = [ ]
        self.assertEqual(actual, expected)
    
    def test_mutiple_match(self) -> None:
        """Test contains_keyword with the keyword appearing in both
        the title or abstract of mutiple articles.
        """
        actual = arxiv_functions.contains_keyword(TEST_ARXIV, 'We')
        expected = ['031', '067', '827', '008']
        self.assertEqual(actual, expected)   
    
    def test_uppercase_match(self) -> None:
        """Test contains_keyword with the keyword appearing in both
        the title or abstract of mutiple articles but in uppercase.
        """
        actual = arxiv_functions.contains_keyword(TEST_ARXIV, 'WE')
        expected = ['031', '067', '827', '008']
        self.assertEqual(actual, expected) 
    
    def test_empty_string(self) -> None:
        """Test contains_keyword with the keyword being an empty string.
        """
        actual = arxiv_functions.contains_keyword(TEST_ARXIV, '')
        expected = [ ]
        self.assertEqual(actual, expected) 
    
    def test_empty_string(self) -> None:
        """Test contains_keyword with the keyword being an empty string.
        """
        actual = arxiv_functions.contains_keyword(TEST_ARXIV, '')
        expected = [ ]
        self.assertEqual(actual, expected)  
    
    def test_non_alphbetic_letter(self) -> None:
        """Test contains_keyword with the keyword being an non_alphbetic_letter.
        """
        actual = arxiv_functions.contains_keyword(TEST_ARXIV, '2')
        expected = [ ]
        self.assertEqual(actual, expected)  
    
    def test_words_with_whitespace(self) -> None:
        """Test contains_keyword with the keyword with whitespace in between 
        but it is in the title or/and abstract of an article.
        """
        actual = arxiv_functions.contains_keyword(TEST_ARXIV, 'Calculus is')
        expected = ['031']
        self.assertEqual(actual, expected)       
                              
if __name__ == '__main__':
    unittest.main(exit=False)
