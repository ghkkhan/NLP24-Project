# the idea here is to either use stuff from the movie_reviews corpus OR 
# from the IMDB collection of text 
from src.name_detection import get_name_array, get_all_names, get_noun_array
from src.text_reading import get_corpus_text, get_imdb_text
from src.tmdb_api import get_common_films_from_name_array
from src.title_detection import is_title_in_review

import sys 


def get_films_from_review(source):

    review_text = ""
    if (source == "corpus"):
        # this will change depending on the argument provided 
        review_text = get_corpus_text()
    elif (source == "imdb"):
        review_text = get_imdb_text()
        

    print("Getting the names from the review...")
    name_array = get_name_array(review_text)
    name_set = set(name_array)


    #print(movie_reviews.raw(the_file))
    print(review_text)
    print("The above review is of one of these possibilities:")
    #print(potential_titles)

    print(f"Potential names detected: {len(name_set)}")
    potential_titles = get_common_films_from_name_array(name_set)

    for potential_title in potential_titles:
        potential_title["Title In Review"] = is_title_in_review(review_text, potential_title["Title"])

    answer_strings = []
    for index, title in enumerate(potential_titles):
        if index > 10:
            break
        answer_strings.append(f"Title: {title["Title"]} | Title In Review: {title["Title In Review"]} | Cast/Crew Connections: {title["Appears"]}")

    return answer_strings

if __name__ == "__main__":
    # holds corpus or imdb 
    source = sys.argv[1]

    print(source)
    if (source == "corpus" or source == "0"):
        answers = get_films_from_review(source="corpus")
    elif source == "imdb" or  source == "1":
        answers = get_films_from_review(source="imdb")
    [print(answer) for answer in answers]