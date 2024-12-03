import spacy  # type: ignore

nlp = spacy.load("en_core_web_sm")

import nltk  # type: ignore
import random
import os
from nltk.corpus import movie_reviews  # type: ignore
from nltk.corpus import names  # type: ignore
from nltk import word_tokenize, pos_tag, ne_chunk  # type: ignore

from src.tmdb_api import get_common_films_from_name_array
from src.text_reading import get_corpus_text, get_imdb_text


def get_all_names():
    male_names = names.words("male.txt")
    female_names = names.words("female.txt")
    all_names_capitalized = set(male_names + female_names)
    all_names = {name.lower() for name in all_names_capitalized}
    return all_names


# using spacy
def get_name_array(review_text):
    # SPACY-TUTORIAL: https://www.wisecube.ai/blog/named-entity-recognition-ner-with-python/

    # define the named entity categories that we want to recognize
    ner_categories = ["PERSON", "ORG", "GPE", "PRODUCT"]

    doc = nlp(review_text)
    # print(review)
    entities = []
    for ent in doc.ents:
        if ent.label_ in ner_categories:
            entities.append((ent.text, ent.label_))

    name_array = []
    for entity, category in entities:
        print(f"{entity}: {category}")
        name_array.append(entity)

    return name_array


# call this if the name array is disappointing 
def get_noun_array(review_text):
    doc = nlp(review_text)
    return [token.text for token in doc if token.pos_ == "NOUN"]
