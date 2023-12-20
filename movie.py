api_key = "8bf41bd8dd79b79f2cce125f6eb2bda0"

import requests
import json

def get_movie_details():
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
    parameter = {"api_key": api_key, "query": "Harry Potter"}
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


    print(results['title'])
    # print(results['tagline'])
    print('-'*10)
    print(results['overview'])
    # for genre in results['genres']:
    #     print(f'- {genre["name"]}')
    print("Starring:")
    count = 0
    cast = []
    for star in movie_credits_results["cast"]:
        if count == 5:
            break
        print(f'* {star["name"]}')
        count += 1
        cast.append(star["name"])

    movie_output = {'title': results['title'], 'cast': cast}

    return movie_output

get_movie_details()