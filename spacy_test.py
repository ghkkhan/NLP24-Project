import spacy
nlp = spacy.load("en_core_web_sm")

import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import names
from nltk import word_tokenize, pos_tag, ne_chunk

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

# text = "Robert Downey Jr. is an american actor and producer. He is best known for his rolesin  films such as Iron Man, The Avengers, and sherlock holmes. Downey has won several awards for his acting, including two screen actors guild awards and a golden globe award. he has also been nominated for an academy award."
# text = """ director andrew davis reworks his fugitive formula and the results are about as exciting as his last film -- the dreadful comedy steal big , steal little -- was funny . keanu " i ' d rather play music than play another action hero " reeves is the grad student on the run , who , along with his superfluous sidekick ( rachel weisz ) , has been framed for a sabotaged science experiment that vaporized eight chicago city blocks . ( the mushroom - cloud explosion is a knock - out and easily the best part of the movie . or , as one audience member succinctly summed it up : " whoa . " ) false information implicates their involvement and boy and girl are soon on the run , fleeing over open drawbridges , across icy lakes , and through the corridors of power at a top - secret , underground energy facility . aiding and abetting is the team ' s shady mentor , played in an excellent - but - so - what performance by morgan freeman . ( brit brian cox is also about , as the behind - the - scenes bad guy . he has some fun fiddling with a southern accent . ) unfunny , overscored , and without a single shred of suspense , chain reaction is * the * summer movie to walk out on . if you make it to the end , a mess of cross - cutting involving another imminent explosion , you ' ll hear somebody say " i guess it ' s time to go . " heed that warning"""
doc = nlp(review)
print(review)
entities = []
for ent in doc.ents:
    if ent.label_ in ner_categories:
        entities.append((ent.text, ent.label_))

entityset = set(entities)
for entity, category in entities:
    print(f"{entity}: {category}")
