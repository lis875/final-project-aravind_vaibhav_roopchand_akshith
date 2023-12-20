from config import TMDB_API_KEY

api_key = TMDB_API_KEY

import requests
import json

def get_movie_details(movie_name):
    ##### Useful URLS
    # Base URL for accessing the TMBD API
    movies_base= "https://api.themoviedb.org/3/"

    # URL for getting information about the the Marvels (movie id 609681)
    marvels = movies_base + "movie/945729"

    # Additional URLS for searching
    people_search = movies_base + "search/person"
    movie_search = movies_base + "search/movie"

    ##### Code for accessing TMBD

    # Request information about the Marvels, and pass the api_key as a parameter
    parameter = {"api_key": api_key, "query": movie_name}
    result_json = requests.get(movie_search, parameter)

    # Convert the results from JSON to a dictionary
    results = json.loads(result_json.text)
    try:
        results = results['results'][0]
    except:
        parameter = {"api_key": api_key, "query": 'The Killer'}
        result_json = requests.get(movie_search, parameter)

        # Convert the results from JSON to a dictionary
        results = json.loads(result_json.text)
        results = results['results'][0]
    movie_id = results['id']

    movie_credits = movies_base + f"movie/{movie_id}/credits"

    movie_credits_result_json = requests.get(movie_credits, parameter)

    # Convert the results from JSON to a dictionary
    movie_credits_results = json.loads(movie_credits_result_json.text)

    # Pretty print the dictionary so we can see what it looks like


    # print(results['title'])
    # print(results['tagline'])
    # print('-'*10)
    # print(results['overview'])
    # for genre in results['genres']:
    #     print(f'- {genre["name"]}')
    # print("Starring:")
    count = 0
    cast = ''
    for star in movie_credits_results["cast"]:
        if count == 5:
            break
        # print(f'* {star["name"]}')
        count += 1
        # cast.append(star["name"])
        cast += ', ' + star['name']

    movie_output = {'title': results['title'], 'cast': str(cast)}

    return movie_output

# print(get_movie_details("Harry"))