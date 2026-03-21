import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics.pairwise import cosine_similarity
movies = pd.read_csv('data/processed_movies.csv', index_col=0)


vectorizer = CountVectorizer(stop_words='english')
vectors = vectorizer.fit_transform(movies['tags'])

similarity = cosine_similarity(vectors)

"""
            Avatar   Titanic   Batman
Avatar      1.0       0.1       0.8
Titanic     0.1       1.0       0.2
Batman      0.8       0.2       1.0
"""
def recommend(movie, n_recommendations):
    movie = movie.capitalize()
    try:
        movie_index = movies[movies['title'].str.contains(movie, case=False)].index[0]
    except IndexError:
        print(f'Movie "{movie}" not found in the dataset.')
        return

    similarity_score = similarity[movie_index]

    similarity_sorted = enumerate(similarity_score)
    similarity_sorted = sorted(similarity_sorted, key=lambda x: x[1], reverse=True)
    top_n_movies = similarity_sorted[1:1 + n_recommendations]
    return top_n_movies




