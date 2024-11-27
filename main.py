# the idea here is to either use stuff from the movie_reviews corpus OR 
# from the IMDB collection of text 
from src.spacy_test import get_films_from_review

import sys 

if __name__ == "__main__":
    # holds corpus or imdb 
    source = sys.argv[1]

    print(source)
    if (source == "corpus" or source == "0"):
        print(get_films_from_review(source="corpus")) 
    elif source == "imdb" or  source == "1":
        print(get_films_from_review(source="imdb")) 