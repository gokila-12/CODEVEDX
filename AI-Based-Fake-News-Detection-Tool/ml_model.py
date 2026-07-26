import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from colorama import Fore

from data_manager import read_data

MODEL_FILE = "fake_news_model.pkl"


def _train_and_save_model(df):
   
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(df["Text"])
    y = df["Label"]

    clf = LogisticRegression(max_iter=1000)
    clf.fit(X, y)

    with open(MODEL_FILE, "wb") as f:
        pickle.dump((vectorizer, clf), f)

    return vectorizer, clf


def predict_news():
    
    df = read_data()

    if len(df) < 6:
        print(Fore.YELLOW + "⚠️ Not enough training data.")
        return

    try:
        vectorizer, clf = _train_and_save_model(df)

        news_text = input(Fore.CYAN + "\nEnter news text to check: ").strip()
        if not news_text:
            print(Fore.RED + "❌ News text cannot be empty.")
            return

        X_input = vectorizer.transform([news_text])
        prediction = clf.predict(X_input)[0]
        probabilities = clf.predict_proba(X_input)[0]
        confidence = max(probabilities) * 100

        color = Fore.GREEN if prediction == "Real" else Fore.RED
        icon = "✅" if prediction == "Real" else "🚨"

        print(color + f"\n{icon} Prediction: {prediction}")
        print(color + f"Confidence: {confidence:.2f}%\n")

    except Exception as e:
        print(Fore.RED + f"Error during prediction: {e}")
