import spacy # type: ignore
nlp = spacy.load("en_core_web_sm")

import nltk # type: ignore
import random
from nltk.corpus import movie_reviews # type: ignore
from nltk.corpus import names # type: ignore
from nltk import word_tokenize, pos_tag, ne_chunk # type: ignore

from tmdb_api import get_common_films_from_name_array

male_names = names.words("male.txt")
female_names = names.words("female.txt")
all_names_capitalized = set(male_names + female_names)
all_names = {name.lower() for name in all_names_capitalized}

all_files = movie_reviews.fileids()
the_file = random.choice(all_files)

review = " ".join(list(movie_reviews.words(the_file)))



# SPACY-TUTORIAL: https://www.wisecube.ai/blog/named-entity-recognition-ner-with-python/

# define the named entity categories that we want to recognize 
ner_categories = ['PERSON', "ORG", "GPE", "PRODUCT"]

doc = nlp(review)
#print(review)
entities = []
for ent in doc.ents:
    if ent.label_ in ner_categories:
        entities.append((ent.text, ent.label_))

entityset = set(entities)
name_array = []
for entity, category in entities:
    print(f"{entity}: {category}")
    name_array.append(entity)

print(f"Formattable names detected: {len(name_array)}")
potential_titles = get_common_films_from_name_array(name_array)


print(movie_reviews.raw(the_file))
print("The above review is of one of these possibilities:")
#print(potential_titles)

for index, title in enumerate(potential_titles):
    if index > 10:
        break
    print(f"{title["Title"]} ({title["Appears"]})")
