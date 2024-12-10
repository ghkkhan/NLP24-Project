import os
import json
import requests
from bs4 import BeautifulSoup

dir_to_aclImdb = "./aclImdb"


def get_sorted_reviews(directory):
    return sorted(os.listdir(directory), key=lambda x: int(x.split('_')[0]))

def extract_titles_id(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    lines_to_return = [line.strip() for line in lines]
    lines_to_return = [l.split("/")[-2] for l in lines]
    return(lines_to_return)


train_neg_reviews = get_sorted_reviews(os.path.join(dir_to_aclImdb, "train/neg"))
train_pos_reviews = get_sorted_reviews(os.path.join(dir_to_aclImdb, "train/pos"))
test_neg_reviews = get_sorted_reviews(os.path.join(dir_to_aclImdb, "test/neg"))
test_pos_reviews = get_sorted_reviews(os.path.join(dir_to_aclImdb, "test/pos"))

# Extract title ids
train_titles_neg = extract_titles_id(os.path.join(dir_to_aclImdb, "train/urls_neg.txt"))
train_titles_pos = extract_titles_id(os.path.join(dir_to_aclImdb, "train/urls_pos.txt"))
test_titles_neg = extract_titles_id(os.path.join(dir_to_aclImdb, "test/urls_neg.txt"))
test_titles_pos = extract_titles_id(os.path.join(dir_to_aclImdb, "test/urls_pos.txt"))

review_title_map = {}

datasets = [
    (train_neg_reviews, train_titles_neg, "train/neg"),
    (train_pos_reviews, train_titles_pos, "train/pos"),
    (test_neg_reviews, test_titles_neg, "test/neg"),
    (test_pos_reviews, test_titles_pos, "test/pos")
]

for review_list, title_list, directory in datasets:
    for filename, title_id in zip(review_list, title_list):
        with open(os.path.join(dir_to_aclImdb, directory, filename), 'r') as file:
            content = file.read().strip()
        review_title_map[content] = title_id

with open('review_title_map.json', 'w') as json_file:
    json.dump(review_title_map, json_file)


with open('review_title_map.json', 'r') as json_file:
    review_title_map = json.load(json_file)


def get_movie_title(imdb_id):
    url = f"https://www.imdb.com/title/{imdb_id}/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Error: Unable to fetch the page (status code: {response.status_code})"

    soup = BeautifulSoup(response.text, 'html.parser')
    title_tag = soup.find('title')

    if title_tag:
        title = title_tag.text.replace(" - IMDb", "").strip()
        return title
    else:
        return "Error: Movie title not found"

# Get title from a IMDB movie review:
get_movie_title(review_title_map["This movie was sadly under-promoted but proved to be truly exceptional. Entering the theatre I knew nothing about the film except that a friend wanted to see it.<br /><br />I was caught off guard with the high quality of the film. I couldn't image Ashton Kutcher in a serious role, but his performance truly exemplified his character. This movie is exceptional and deserves our monetary support, unlike so many other movies. It does not come lightly for me to recommend any movie, but in this case I highly recommend that everyone see it.<br /><br />This films is Truly Exceptional!"])