#Movie recommender
A content based movie recommender system with a CLI interface

##Features
- Recommend movies based on user input
- Choose how many movies to recommend
- Show the simmilarity percentage
- CLI interface with "quit" command to exit

##Dataset
- tmdb_5000_credits.csv
- tmdb_5000_movies.csv
These datasets are merged an preprocessed into processed_movies.csv

##Tech Stack
- Python
- pandas
- scikit-learn
- CountVectorizer
- Cosine similarity

##How it works
- load_data.py procces the 2 datasets and transform them into "processed_movies.csv"
- A "tags" column is created combining:
    - keywords
    - cast
    - director
    - genres
    - overview
- CountVectorizer converts the text into numerical vectors
- Cosine_similarity computes similarity between movie vectors
- The system returns the top N most popular movies

##How to run
python src/main.py

##Example
Type the movie you want to see recommendations of (or 'quit' to exit): avatar
How many recommendations do you want? 5
Top 5 movies similar to 'avatar':
1: Titan A.E. (20.80%)
2: Aliens vs Predator: Requiem (19.01%)
3: Aliens (18.79%)
4: Battle: Los Angeles (18.63%)
5: Independence Day (18.58%)

##Future improvements
- Add fuzzy matching for movie title to handle typos
- Build a graphical user interface
- Add poster display
- Add user ratings and personalized recommendations
- Implement recommendation based on similar users
