import recommender

while True:
    movie = input("Type the movie you want to see recommendations of (or 'quit' to exit): ")
    if movie == "quit":
        break
    movies =recommender.recommend(movie)
    if movies:
        print(f"Top 5 movies similar to '{movie}':")
        for i, (index, score) in enumerate(movies):
            print(f"{i + 1}: {recommender.movies.iloc[index]['title']} ({score * 100:.2f}%)")