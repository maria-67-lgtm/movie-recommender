import recommender

while True:
    movie = input("Type the movie you want to see recommendations of (or 'quit' to exit): ")
    if movie == "quit":
        break
    n_recommendations = input("How many recommendations do you want? ")
    if not n_recommendations.isdigit():
        print("Please enter a valid number for recommendations.")
        continue
    n_recommendations = int(n_recommendations)

    
    movies =recommender.recommend(movie, n_recommendations)
    if movies:
        print(f"Top {n_recommendations} movies similar to '{movie}':")
        for i, (index, score) in enumerate(movies):
            print(f"{i + 1}: {recommender.movies.iloc[index]['title']} ({score * 100:.2f}%)")