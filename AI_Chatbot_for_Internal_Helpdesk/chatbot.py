import json
import joblib

# Load model
model = joblib.load("models/chatbot_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

with open("data/intents.json") as file:
    intents = json.load(file)


def get_response(message):

    X = vectorizer.transform([message])

    prediction = model.predict(X)[0]

    for intent in intents:
        if intent["intent"] == prediction:
            return intent["response"]

    return "Sorry, I couldn't understand."