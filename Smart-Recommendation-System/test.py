from utils.recommender import recommend

results = recommend("Interstellar")

print("\nRecommendations:\n")

for movie in results:
    print(
        f"{movie['title']} | "
        f"{movie['genre']} | "
        f"{movie['score']}%"
    )