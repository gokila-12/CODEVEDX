import os
import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# Load dataset
df = pd.read_csv("datasets/movies.csv")

# Combine important text features
df["content"] = (
    df["title"].fillna("") + " " +
    df["genre"].fillna("") + " " +
    df["description"].fillna("")
)

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["content"])

# Cosine Similarity Matrix
similarity = cosine_similarity(tfidf_matrix)

# Save trained models
joblib.dump(tfidf, "models/tfidf.pkl")
joblib.dump(similarity, "models/similarity.pkl")
joblib.dump(df, "models/movies.pkl")

print("=" * 50)
print(" Smart Recommendation Model Trained Successfully!")
print("=" * 50)
print(f"Total Movies : {len(df)}")
print("TF-IDF Model Saved")
print("Similarity Matrix Saved")
print("Dataset Saved")