import requests #type: ignore
import os 
import json
from collections import Counter
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.getenv("TMDB_AUTH")}"
}

# returns result from querying tmdb for person information
# NOTE: returns array of results. if two notable people have the same name, need to figure out how to differentiate 
def get_person_id_by_name(name):
    name = name.replace(" ", "%20")
    url = f"https://api.themoviedb.org/3/search/person?query={name}&include_adult=false&language=en-US&page=1"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        results = data["results"]
        top_results = []
        for result in results:
            if len(top_results) == 3:
                break
            top_results.append(result["id"])
        return top_results
    else:
        return response.status_code

#look ahead determines whether to look at more than 1 person
def get_relevent_info_from_id(id_list,look_at_duplicate_names=False):
    # WHAT IS RELEVENT INFO? 
    # This can change, this is simply the process of getting details from tmdb 
    ## demographics 
    ## -- gender
    ## filmography 
    ## -- title
    ## -- job (actor, director, writer, etc.)

    # this limits to looking for first result from a given name query
    if len(id_list) == 0:
        return []
    if not look_at_duplicate_names:
        id_list = [id_list[0]]

    def get_gender_from_number(num):
        gender_map = {
            0: "Unknown",
            1: "Female", 
            2: "Male", 
            3: "Non-binary"
        }

        return gender_map.get(num, "Unknown")

    # holds info for those in array 
    info_array = []

    ## INFO INIT
    for id in id_list:
        info = dict()
        info_array.append(info)

    ## DETAILS QUERY 
    #### This is where personal information is obtained
    for index, id in enumerate(id_list):
        url = f"https://api.themoviedb.org/3/person/{id}?language=en-US"
        response = requests.get(url, headers=headers)
        res_as_dict = response.json()
        gender = get_gender_from_number(res_as_dict["gender"])
        #print(json.dumps(response.json(), indent=4))

        info_array[index]["Name"] = res_as_dict["name"]
        info_array[index]["Gender"] = gender
    
    ## MOVIE CREDITS QUERY 
    for index, id in enumerate(id_list):
        url = f"https://api.themoviedb.org/3/person/{id}/movie_credits?language=en-US"
        response = requests.get(url, headers=headers)
        res_as_dict = response.json()

        cast_credits = res_as_dict["cast"]
        crew_credits = res_as_dict["crew"]

        # the cast and crew id lists are sets because I don't care 
        # if a person is both a writer and a director  

        cast_id_list = set()
        for cast_credit in cast_credits:
            cast_id_list.add(cast_credit["id"])
        info_array[index]["Cast_Id_List"] = list(cast_id_list)

        crew_id_list = set() 
        for crew_credit in crew_credits:
            crew_id_list.add(crew_credit["id"])
        info_array[index]["Crew_Id_List"] = list(crew_id_list)

        # combined credits 
        credit_id_list = cast_id_list.union(crew_id_list)
        info_array[index]["Credit_Id_List"] = credit_id_list

    return info_array
def get_film_title_from_id(film_id):
    url = f"https://api.themoviedb.org/3/movie/{film_id}?language=en-US"
    response = requests.get(url, headers=headers)
    res_as_dict = response.json()
    return res_as_dict["title"]


def get_common_films(person_list):


    # contains the IDs from cast, crew 
    all_film_ids = []

    for person in person_list:
        #all_film_ids += person[0]["Cast_Id_List"] + person[0]["Crew_Id_List"]
        all_film_ids += person[0]["Credit_Id_List"]
    

    counter = Counter(all_film_ids) # counts how many of each item there are 

    all_ids_counted = [(number, count) for number, count in counter.items()]
    all_ids_counted_sorted = sorted(all_ids_counted, key=lambda x: x[1], reverse=True)

    all_titles = []
    for film_id in all_ids_counted_sorted:
        if film_id[1] < 2: 
            break
        title_with_appearances = dict()
        title_with_appearances["Title"] = get_film_title_from_id(film_id[0])
        title_with_appearances["Appears"] = film_id[1]
        all_titles.append(title_with_appearances)

    return all_titles

def get_common_films_from_name_array(name_array):
    
    person_array = []
    # name_array should be an array of fname, lname pairs
    for name in name_array:
        person_id_list = get_person_id_by_name(name)
        first_person_info = get_relevent_info_from_id(person_id_list)
        if len(first_person_info) == 0:
            continue
        person_array.append(first_person_info)
    
    return get_common_films(person_array)


def main():
    david_lynch_ids = get_person_id_by_name("chris", "hemsworth")
    david = get_relevent_info_from_id(david_lynch_ids)

    kyle_maclachlan_ids = get_person_id_by_name("chris", "evans")
    kyle = get_relevent_info_from_id(kyle_maclachlan_ids)

    person_list = []
    person_list.append(david)
    person_list.append(kyle)

    get_common_films(person_list)

if __name__ == "__main__":
    main()
