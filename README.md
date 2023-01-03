# Metadata
Task 1: Working with ArxivType and using a helper function
1. The first parameter represents arxiv metadata. The second is an article ID and the third is a year. This function will return True if and only if an article with this id occurs in the metadata and was published in this year. 
2. The first parameter represents arxiv metadata. The second is a word to search for in the metadata. This function should return a list of the IDs of articles that contain this keyword in their title and/or abstract. The list should be sorted in lexicographic order.

Task 2: Reading in the arxiv metadata file
The parameter represents an arxiv metadata file that is already open for reading. This function should read the file and return the data in the ArxivType dictionary format. 

Task 3: Working with Authors and Coauthors
1. The parameter represents arxiv metadata. This function should return a dictionary that maps each author name to a list of identifiers of articles written by that author. The list should be sorted in lexicographic order.
2. The first parameter represents arxiv metadata and the second parameter represents an author's name. This function should return a list of coauthors of the author specified by the second argument. (Two people are coauthors if they are authors of the same article.) The list should be sorted in lexicographic order.
3. The parameter represents arxiv metadata. This function should return a list of authors who published the most articles. Note that this list has more than one author only in case of a tie! The list should be sorted in lexicographic order.
4. The first parameter represents arxiv metadata and the second parameter represents the author's name. This function should return a list of authors with whom the author specified by the second argument is encouraged to collaborate. The list should be sorted in lexicographic order.

Task 4: Prolific Authors
1. Create a dictionary that maps author names to a list of IDs of articles published by that author in the first parameter, information on a single article in the second parameter and the third parameter represents the minimum number of publications required for an author to be considered prolific. The function will return True if and only if the article (second argument) has at least one author who is considered prolific.
2. The first parameter represents arxiv metadata and the second parameter represents the minimum number of publications required for an author to be considered prolific. The function should modify its first argument so that it contains only articles published by prolific authors, i.e., articles that have at least one author who has published at least the minimum required number of articles.

Task 5: Required Testing
write a set of unittests and make sure at least one of them would fail on the buggy version of the funcion 
