import os
import pandas as pd

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to movies.csv
MOVIES_FILE = os.path.join(BASE_DIR, "datasets", "movies.csv")

# Load dataset
df = pd.read_csv(MOVIES_FILE)

def recommend(title):
    recommendations = []

    # Find the selected movie
    movie = df[df["title"].str.lower() == title.lower()]

    # If movie not found
    if movie.empty:
        return recommendations

    # Get the selected movie's genre
    genre = movie.iloc[0]["genre"]

    # Find similar movies (same genre)
    similar_movies = df[
        (df["genre"] == genre) &
        (df["title"].str.lower() != title.lower())
    ]

    # Convert similar movies into a list
    for _, row in similar_movies.iterrows():
        recommendations.append({
            "title": row["title"],
            "genre": row["genre"],
            "year": row["year"],
            "rating": row["rating"],
            "poster": row["poster"],
            "description": row["description"]
        })

    return recommendations