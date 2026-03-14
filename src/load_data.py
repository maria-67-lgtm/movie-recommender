import pandas as pd
import ast

movie_data = pd.read_csv('data/tmdb_5000_movies.csv')
credits_data = pd.read_csv('data/tmdb_5000_credits.csv')

movies = movie_data.merge(credits_data, left_on='id', right_on='movie_id', how='left')

movies = movies[['movie_id', 'title_x', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies = movies.dropna()
movies = movies.rename(columns={'title_x': 'title'})


def convert_to_list(text):
    text = ast.literal_eval(text)
    return text

def get_names(text):
    names = []
    for item in text:
        names.append(item['name'])
    return names

def get_top_3_cast(text):
    names = []
    for item in text:
        names.append(item['name'])
    return names[:3]

def get_director(text):
    director = []
    for item in text:
        if item['job'] == 'Director':
            director.append(item['name'])
    return director

def normalize_list(text):
    normalized_text = []
    for item in text:
        item = item.replace(" ", "")
        normalized_text.append(item)
    return normalized_text



movies['genres'] = movies['genres'].apply(convert_to_list)
movies['genres'] = movies['genres'].apply(get_names)
movies['genres'] = movies['genres'].apply(normalize_list)

movies['keywords'] = movies['keywords'].apply(convert_to_list)
movies['keywords'] = movies['keywords'].apply(get_names)
movies['keywords'] = movies['keywords'].apply(normalize_list)

movies['cast'] = movies['cast'].apply(convert_to_list)
movies['cast'] = movies['cast'].apply(get_top_3_cast)
movies['cast'] = movies['cast'].apply(normalize_list)


movies['crew'] = movies['crew'].apply(convert_to_list)
movies['director'] = movies['crew'].apply(get_director)
movies['director'] = movies['director'].apply(normalize_list)

movies['overview'] = movies['overview'].apply(str.split)

movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['director']
movies['tags'] = movies['tags'].apply(" ".join)
movies['tags'] = movies['tags'].apply(str.lower)

movies = movies[['movie_id', 'title', 'tags']]

print(movies[['title', 'tags']].head())

movies.to_csv("data/processed_movies.csv")



