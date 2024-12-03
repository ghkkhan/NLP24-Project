import nltk 
import random
import os
from nltk.corpus import movie_reviews 
from nltk.corpus import names 
from nltk import word_tokenize, pos_tag, ne_chunk 

def get_corpus_text():
    all_files = movie_reviews.fileids()
    the_file = random.choice(all_files)
    review = " ".join(list(movie_reviews.words(the_file)))
    return review

def get_imdb_text():
    directory = "aclImdb/test/pos/"
    files = [
        f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))
    ]
    if files:
        file = random.choice(files)
        with open(os.path.join(directory, file), "r") as fi:
            content = fi.read()
            return content
