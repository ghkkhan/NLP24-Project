import spacy # type: ignore
nlp = spacy.load("en_core_web_sm")

import nltk # type: ignore
import random
from nltk.corpus import movie_reviews # type: ignore
from nltk.corpus import names # type: ignore
from nltk import word_tokenize, pos_tag, ne_chunk # type: ignore

from tmdb_api import get_common_films_from_name_array


def get_all_names():
    male_names = names.words("male.txt")
    female_names = names.words("female.txt")
    all_names_capitalized = set(male_names + female_names)
    all_names = {name.lower() for name in all_names_capitalized}
    return all_names
    

def get_corpus_text():
    all_files = movie_reviews.fileids()
    the_file = random.choice(all_files)
    review = " ".join(list(movie_reviews.words(the_file)))
    return review

def get_imdb_text():
    

def get_name_array(review_text):
    # SPACY-TUTORIAL: https://www.wisecube.ai/blog/named-entity-recognition-ner-with-python/

    # define the named entity categories that we want to recognize 
    ner_categories = ['PERSON', "ORG", "GPE", "PRODUCT"]

    doc = nlp(review_text)
    #print(review)
    entities = []
    for ent in doc.ents:
        if ent.label_ in ner_categories:
            entities.append((ent.text, ent.label_))

    name_array = []
    for entity, category in entities:
        print(f"{entity}: {category}")
        name_array.append(entity)
    return name_array



def get_films_from_review(source):
    
    all_names = get_all_names()

    review_text = ""
    if (source == "corpus"):
        # this will change depending on the argument provided 
        review_text = get_corpus_text()
    elif (source == "imdb"):
        review_text = get_corpus_text()
        

    name_array = get_name_array(review_text)

    #print(movie_reviews.raw(the_file))
    print(review_text)
    print("The above review is of one of these possibilities:")
    #print(potential_titles)

    print(f"Formattable names detected: {len(name_array)}")
    potential_titles = get_common_films_from_name_array(name_array)



    answer_strings = []
    for index, title in enumerate(potential_titles):
        if index > 10:
            break
        answer_strings.append(f"{title["Title"]} ({title["Appears"]})")
    return answer_strings