# 🎬 AI Stream — Smart Movie Recommendation System

<p align="center">
  <b>AI-powered movie discovery and recommendation platform</b>
</p>

<p align="center">
  Built with Python, Flask, Machine Learning, HTML, CSS and JavaScript.
</p>

---

## 📖 About

**AI Stream** is a web-based Smart Movie Recommendation System designed to help users discover movies through an interactive, streaming-style interface.

The application combines a Flask web backend with a machine-learning recommendation system. Users can browse movies, search for titles, view detailed movie information, receive recommendations, create accounts, manage favorites, and maintain a personal watchlist.

The recommendation engine uses **TF-IDF Vectorization** and **Cosine Similarity** to find movies related to the selected movie.

---

##Demo Video


https://github.com/user-attachments/assets/95bf4831-cb02-4a76-8955-85c88e1b4daa



## ✨ Features

### 🎬 Movie Discovery

- 🔥 Trending movies
- ⭐ Top-rated movies
- 🤖 AI movie recommendations
- 🔎 Movie search
- 🎥 Movie details
- ⏳ Continue Watching interface
- 🎭 Genre-based browsing

### 👤 User Account

- 📝 User registration
- 🔐 User login
- 🚪 Logout
- ❤️ Favorite movies
- 📋 Personal watchlist
- 🗑️ Remove movies from watchlist

### 🧠 Recommendation System

- TF-IDF text vectorization
- Cosine similarity
- Content-based recommendations
- Genre-based recommendations
- Pre-trained model storage using Joblib

### 📊 Admin Dashboard

- Total movies
- Total registered users
- Total watchlist entries

---

## 🧠 How It Works

The recommendation system uses movie metadata such as the **title, genre, and description**.

```text
Movie Dataset
     │
     ▼
Title + Genre + Description
     │
     ▼
TF-IDF Vectorization
     │
     ▼
Feature Matrix
     │
     ▼
Cosine Similarity
     │
     ▼
Recommended Movies

```

## project Structure
```text
Smart-Recommendation-System/
│
├── datasets/
│   └── movies.csv
│
├── models/
│   ├── movies.pkl
│   ├── tfidf.pkl
│   └── similarity.pkl
│
├── static/
│   ├── images/
│   │   └── posters/
│   ├── style.css
│   └── js/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── result.html
│   ├── details.html
│   ├── search.html
│   ├── watchlist.html
│   └── admin.html
│
├── utils/
│   └── recommender.py
│
├── app.py
├── database.py
├── train.py
├── test.py
└── users.db

```
##Tech Stack
## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Flask | Web framework |
| Pandas | Dataset processing |
| Scikit-learn | Machine learning |
| TF-IDF | Text vectorization |
| Cosine Similarity | Recommendation algorithm |
| Joblib | Model storage |
| SQLite | Database |
| Flask-Bcrypt | Password hashing |
| HTML5 | Frontend |
| CSS3 | Styling |
| JavaScript | Frontend functionality |
| Jinja2 | Template rendering |

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/gokila-12/CODEVEDX.git
cd CODEVEDX/Smart-Recommendation-System
```
```bash
pip install flask pandas scikit-learn  flask-bcrypt
```
```bash
python train.py
python app.py
```
## 🎥 Current Status

The current version provides the movie discovery and recommendation experience, including movie details, search, favorites, watchlist, authentication, and recommendation features.

The **Watch**, **Watch Now**, and **Continue** buttons are currently part of the interface. Actual movie/video playback is planned for a future version.

## 🔮 Future Improvements

- 🎥 Actual movie/video playback
- ▶️ HTML5 video player
- 🤖 More personalized recommendations
- 👥 Collaborative filtering
- ⭐ User ratings and reviews
- 👤 User profiles
- 🎭 Cast and director information
- 📱 Improved mobile responsiveness
- ☁️ Online deployment
- 📈 Recommendation analytics

  ## 👨‍💻 Author

**Gokila Krishna B**

GitHub:  
https://github.com/gokila-12



