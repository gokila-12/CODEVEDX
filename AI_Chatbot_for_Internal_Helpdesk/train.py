import json
import joblib

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load intents
with open("data/intents.json", "r") as file:
    intents = json.load(file)

training_sentences = []
training_labels = []

for intent in intents:
    for pattern in intent["patterns"]:
        training_sentences.append(pattern)
        training_labels.append(intent["intent"])

# Vectorizer
vectorizer = CountVectorizer()

X = vectorizer.fit_transform(training_sentences)

# Model
model = MultinomialNB()

model.fit(X, training_labels)

# Save model
joblib.dump(model, "models/chatbot_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model trained successfully!")