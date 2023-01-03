# importing copy for use in the keep_prolific_authors docstring
# you do not need to use it anywhere else
import copy  
from typing import Dict, List, TextIO

from constants import (ID, TITLE, CREATED, MODIFIED, AUTHORS, ABSTRACT, END, 
                       NameType, ArticleValueType, ArticleType, ArxivType)


EXAMPLE_ARXIV = {
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

EXAMPLE_BY_AUTHOR = {
    ('Ponce', 'Marcelo'): ['008', '827'],
    ('Tafliovich', 'Anya Y.'): ['008', '827'],
    ('Bretscher', 'Anna'): ['067', '827'],
    ('Breuss', 'Nataliya'): ['031'],
    ('Pancer', 'Richard'): ['067']
}

################################################
## Task 1 
################################################

# a helper to remove non-alphabetic characters
def clean_word(word: str) -> str:
    """Return word with all non-alphabetic characters removed and converted to 
    lowercase.
    
    Precondition: word contains no whitespace
    
    >>> clean_word('Hello!!!')
    'hello'
    >>> clean_word('12cat.dog?')
    'catdog'
    >>> clean_word("DON'T")
    'dont'
    """
    new_word = ''
    for ch in word:
        if ch.isalpha():
            new_word = new_word + ch.lower()
    return new_word

# Add your other Task 1 functions here
def created_in_year(arxiv_data: ArxivType, ids: str, year: int) -> bool:
    """Return True iff the article with the associated ID was published in speci
    fied year and in the metadata.
    
    >>> created_in_year(EXAMPLE_ARXIV , '067', 2021)
    True
    >>> created_in_year(EXAMPLE_ARXIV , '031', 2021)
    False
    """
    if arxiv_data[ids][CREATED][:4] != '':
        if int(arxiv_data[ids][CREATED][:4]) == year:
            return True
        else:
            return False
    else:
        return False

def contains_keyword(arxiv_data: ArxivType, keyword: str) -> List[str]:
    """Return a list of IDs of articles which consists of the keyword in either
    /both the title or/and abstract.
    Precondition: words contain no whitespace,non-alphabetic characters and leng
    /th greater than one
    
    >> contains_keyword(EXAMPLE_ARXIV, 'Calculus')
    ['031']
    >>> contains_keyword(EXAMPLE_ARXIV, 'Toronto')
    ['827']
    """
    list1 = [ ]
    keyword = clean_word(keyword)
    for articles in arxiv_data:
        if keyword in clean_word(arxiv_data[articles][TITLE]):
            list1.append(articles)
        elif keyword in clean_word(arxiv_data[articles][ABSTRACT]):
            list1.append(articles)   
        if keyword == '':
            list1 = [ ]
    return list1

################################################
## Task 2
################################################

def read_arxiv_file(f: TextIO) -> ArxivType:
    """Return a ArxivType dictionary containing the arxiv metadata in f.

    Note we do not include example calls for functions that take open files.
    """
    
    main_dict = { }  
    line = f.readline().strip()
    while line != '':
        sub_dic = {ID: '', TITLE: '', CREATED: '', MODIFIED:'', AUTHORS: [ ],\
                   ABSTRACT: '' }
        sub_dic[ID] = line
        line = f.readline().strip()
        sub_dic[TITLE] = line
        line = f.readline().strip()
        sub_dic[CREATED] = line
        line = f.readline().strip()
        sub_dic[MODIFIED] = line
        line = f.readline().strip()
        while line != '' :               
            sub_dic[AUTHORS].append(tuple(line.split(",")))
            line = f.readline().strip()
        line = f.readline().strip()
        while line != END:
            sub_dic[ABSTRACT] += line + '\n'
            line = f.readline().strip()
        sub_dic[ABSTRACT] = sub_dic[ABSTRACT][:-1]
        main_dict[sub_dic[ID]] = sub_dic        
        line = f.readline().strip()
    return main_dict
  
################################################
## Task 3
################################################
def make_articles_to_author(id_to_article: ArxivType
                            ) -> Dict[NameType, List[str]]:
    """Return a dict that maps each id of article to a list (sorted in
    lexicographic order) of authors es written by that author,
    based on the information in id_to_article.
    
    >>> make_articles_to_author(EXAMPLE_ARXIV) ['031']
    [('Breuss', 'Nataliya')]
    >>> make_articles_to_author(EXAMPLE_ARXIV) ['008']
    [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')]
    """
    dict1 = {}
    for subdict in id_to_article:
        authors = id_to_article[subdict][AUTHORS]
        ids = subdict
        if ids not in dict1:
            dict1[ids] = authors
    for x in dict1:
        dict1[x].sort()    
    return dict1

def make_author_to_articles(id_to_article: ArxivType
                            ) -> Dict[NameType, List[str]]:
    """Return a dict that maps each author name to a list (sorted in
    lexicographic order) of IDs of articles written by that author,
    based on the information in id_to_article.

    >>> make_author_to_articles(EXAMPLE_ARXIV) == EXAMPLE_BY_AUTHOR
    True
    >>> make_author_to_articles(EXAMPLE_ARXIV)
    {('Breuss', 'Nataliya'): ['031'],\
 ('Bretscher', 'Anna'): ['067', '827'],\
 ('Pancer', 'Richard'): ['067'],\
 ('Ponce', 'Marcelo'): ['008', '827'],\
 ('Tafliovich', 'Anya Y.'): ['008', '827']}
    """
    dict1 = make_articles_to_author(id_to_article)
    dict2 = { }
    for ids in dict1:
        authors = tuple(dict1[ids])
        for author in authors:
            if author not in dict2:
                dict2[author] = [ids]
            else:
                dict2[author].append(ids)
    for x in dict2:
        dict2[x].sort()           
    return dict2

def get_coauthors(arxiv_data: ArxivType, author: NameType) -> List[NameType]:
    """Return a sorted list in  lexicographic order of coauthors that has the 
    author specified in the second arguments
    
    >>> get_coauthors(EXAMPLE_ARXIV, ('Tafliovich', 'Anya Y.'))
    [('Bretscher', 'Anna'), ('Ponce', 'Marcelo')]   
    
    >>> get_coauthors(EXAMPLE_ARXIV, ('Breuss', 'Nataliya'))
    []
    """
    list1 = [ ]
    list2 = [ ]
    for keys in arxiv_data:
        if author in arxiv_data[keys][AUTHORS] :  
            list1.append(tuple(arxiv_data[keys][AUTHORS]))   
            for values in list1:
                for value in values:
                    if value not in list2:
                        list2.append(value)  
    if author in list2:
        list2.remove(author)
    list2.sort()
    return list2
    
def get_most_published_authors(arxiv_data: ArxivType) -> List[NameType]:
    """Return a sorted list of authors in  lexicographic order that have \
    published the most articles, in case of a tie, return those authors.
    
    >>> get_most_published_authors(EXAMPLE_ARXIV)
    [('Bretscher', 'Anna'), ('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')]
    >>>get_most_published_authors(EXAMPLE_ARXIV) == [('Bretscher', 'Anna'),\
    ('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')]
    True
    """
    dic1 = make_author_to_articles(arxiv_data)
    list1 = [ ]
    maximum = 0
    for authors in dic1:        
        articles = dic1[authors]
        if len(articles) >= maximum:
            maximum = len(articles) #2
    for authors in dic1:        
        articles = dic1[authors]   
        if len(articles) == maximum:
            list1.append(authors)   
    list1.sort()
    return list1
def suggest_collaborators(arxiv_data: ArxivType, author: NameType) \
    -> List[NameType]:
    """Return a sorted list in lexicographic order of authors who are being
    suggested to collborate specified in the second arugument
    
    >>> suggest_collaborators(EXAMPLE_ARXIV,('Pancer', 'Richard'))
    [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')]
    >>> suggest_collaborators(EXAMPLE_ARXIV, ('Tafliovich', 'Anya Y.'))
    [('Pancer', 'Richard')]
    """
    list1 = [ ]
    coauthors = get_coauthors(arxiv_data, author) 
    for people in coauthors:              
        connection = get_coauthors(arxiv_data, people)
        for friends in connection:
            if friends not in coauthors:
                list1.append(friends)
    while author in list1:
            list1.remove(author)
    list1.sort()
    return list1
            
################################################
## Task 4
################################################

# Add your Task 4 functions here
def has_prolific_authors(author_id: Dict[NameType, List[str]], \
                         article_id: ArticleType, prolific_requirement: int) \
    -> bool:
    """Return True iff the Article is written by at least one authoor that is 
    considered profilic, in which is being measured by the prolifc requirement
    
    >>> has_prolific_authors({('Ponce', 'Marcelo'): ['008', '827'],\
    ('Tafliovich', 'Anya Y.'): ['008', '827'],\
    ('Bretscher', 'Anna'): ['067', '827'],('Breuss', 'Nataliya'): ['031'],\
    ('Pancer', 'Richard'): ['067']} , EXAMPLE_ARXIV['008'][ID], 2)
    True
    >>> has_prolific_authors({('Ponce', 'Marcelo'): ['008', '827']},\
    EXAMPLE_ARXIV['008'][ID], 2)
    True
    """
    for authors in author_id:
        for articles in author_id[authors]:
            if article_id == articles and len(author_id[authors]) \
               >= prolific_requirement :
                return True
    return False
                
def keep_prolific_authors(id_to_article: ArxivType,
                          min_publications: int) -> None:
    """Update id_to_article so that it contains only articles published by
    authors with min_publications or more articles published. As long
    as at least one of the authors has min_publications, the article
    is kept.

    >>> arxiv_copy = copy.deepcopy(EXAMPLE_ARXIV)
    >>> keep_prolific_authors(arxiv_copy, 2)
    >>> len(arxiv_copy)
    3
    >>> '008' in arxiv_copy and '067' in arxiv_copy and '827' in arxiv_copy
    True
    >>> arxiv_copy = copy.deepcopy(EXAMPLE_ARXIV)
    >>> keep_prolific_authors(arxiv_copy, 3)
    >>> arxiv_copy
    {}
    """
    arxiv_author = make_author_to_articles(id_to_article)    
    for keys, values in list(id_to_article.items()):
            if has_prolific_authors(arxiv_author, \
                values[ID], min_publications) is False:
                del id_to_article[keys]
                  
if __name__ == '__main__':
    pass
   
