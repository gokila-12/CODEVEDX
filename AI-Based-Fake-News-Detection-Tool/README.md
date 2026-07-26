# 📰 AI-Based Fake News Detection

An AI-powered **Fake News Detection System** built using **Machine Learning** and **Natural Language Processing (NLP)**. This project analyzes news articles and predicts whether they are **Real** or **Fake** by preprocessing text data, extracting meaningful features, and using a trained classification model.

---

## 📌 Overview

The rapid spread of misinformation across online platforms has made fake news detection an important research area. This project leverages Machine Learning algorithms to classify news articles based on their textual content, helping users identify potentially misleading information.

---

## ✨ Features

- 🔍 Detects whether a news article is **Real** or **Fake**
- 🧹 Text preprocessing using NLP techniques
- 📊 TF-IDF feature extraction
- 🤖 Machine Learning-based classification
- 💾 Pre-trained model for fast predictions
- ⚡ Simple and easy-to-use Python implementation
- 🔄 Easily extendable with new datasets or models

---

## 🛠️ Tech Stack

- Python 
- Pandas
- Scikit-learn
- NLTK
- Pickle

---

## 📂 Project Structure

```
AI-Based-Fake-News-Detection/
│
├── main.py                 
├── data_manager.py         
├── ml_model.py             
├── fake_news_model.pkl     
├── news_data.csv                  
└── README.md               
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/gokila-12/AI-Based-Fake-News-Detection.git
cd AI-Based-Fake-News-Detection
```

### Install dependencies

```bash
pip install pandas numpy scikit-learn nltk
```

---

## ▶️ How to Run

Run the application:

```bash
python main.py
```

If you need to train the model again:

```bash
python ml_model.py
```

---

## 📊 Dataset

The project uses a CSV dataset containing news articles and their corresponding labels.

| Column | Description |
|---------|-------------|
| text | News article content |
| label | Real or Fake |

---

## 🔄 Project Workflow

```
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Text Preprocessing
   │
   ▼
TF-IDF Vectorization
   │
   ▼
Machine Learning Model
   │
   ▼
Prediction
```

---

## 🧠 Machine Learning Pipeline

1. Load the dataset
2. Clean and preprocess the text
3. Remove stop words and unwanted characters
4. Convert text into numerical features using TF-IDF
5. Train the Machine Learning model
6. Save the trained model
7. Predict whether a news article is Real or Fake

---

## 📸 Example

### Input

```
Scientists have discovered a new renewable energy source capable of powering entire cities.
```

### Output

```
Prediction: Real News ✅
confidence : 65.78%
```

---

## 📈 Future Enhancements

- 🌐 Web application using Flask or Streamlit
- 🤖 Deep Learning models (LSTM, BERT)
- 📱 Mobile application
- 🌍 Multi-language fake news detection
- ☁️ REST API deployment
- 📊 Interactive dashboard and analytics

---
## 👨‍💻 Author

GOKILA KRISHNA B

- GitHub: https://github.com/gokila-12
---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub. It helps others discover the project and motivates future improvements.
