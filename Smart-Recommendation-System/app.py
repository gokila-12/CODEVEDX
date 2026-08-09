from flask import Flask, render_template, request
from utils.recommender import recommend
import joblib
import sqlite3
import os
import pandas as pd

movies_df = pd.read_csv("datasets/movies.csv")
from flask import session, redirect, render_template

from flask import Flask, render_template, request, redirect, session, flash

from flask_bcrypt import Bcrypt

from database import init_db

app = Flask(__name__)
app.secret_key = "AI_STREAM_SECRET"

bcrypt = Bcrypt(app)

init_db()

movies = joblib.load("models/movies.pkl")


@app.route("/")
def home():
    movie_list = sorted(movies["title"].tolist())
    return render_template("index.html", movies=movie_list)


@app.route("/recommend", methods=["POST"])
def recommendation():
    movie = request.form.get("movie")

    recommendations = recommend(movie)

    return render_template(
        "result.html",
        movie=movie,
        recommendations=recommendations
    )
@app.route("/register", methods=["GET","POST"])
def register():

    if request.method=="POST":

        fullname=request.form["fullname"]
        email=request.form["email"]
        password=request.form["password"]
        confirm=request.form["confirm_password"]

        if password!=confirm:

            flash("Passwords do not match!")

            return redirect("/register")

        conn=sqlite3.connect("users.db")

        cursor=conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        )

        user=cursor.fetchone()

        if user:

            flash("Email already exists")

            conn.close()

            return redirect("/register")

        hashed=bcrypt.generate_password_hash(password).decode("utf-8")

        cursor.execute(
            "INSERT INTO users(fullname,email,password) VALUES(?,?,?)",
            (fullname,email,hashed)
        )

        conn.commit()

        conn.close()

        flash("Registration Successful!")

        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method=="POST":

        email=request.form["email"]

        password=request.form["password"]

        conn=sqlite3.connect("users.db")

        cursor=conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        )

        user=cursor.fetchone()

        conn.close()

        if user:

            if bcrypt.check_password_hash(
                user[3],
                password
            ):

                session["user"]=user[1]

                return redirect("/")

        flash("Invalid Email or Password")

    return render_template("login.html")

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")

@app.route("/watchlist/add/<movie>")
def add_watchlist(movie):

    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT email FROM users WHERE fullname=?",
        (session["user"],)
    )

    user = cursor.fetchone()

    if user:

        cursor.execute(
            "INSERT INTO watchlist(email,movie) VALUES(?,?)",
            (user[0], movie)
        )

    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/watchlist")
def watchlist():

    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT email FROM users WHERE fullname=?",
        (session["user"],)
    )

    user = cursor.fetchone()

    movies = []

    if user:

        cursor.execute(
            "SELECT movie FROM watchlist WHERE email=?",
            (user[0],)
        )

        rows = cursor.fetchall()

        movies = [row[0] for row in rows]

    conn.close()

    return render_template(
        "watchlist.html",
        movies=movies
    )
@app.route("/watchlist/delete/<movie>")
def delete_watchlist(movie):

    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT email FROM users WHERE fullname=?",
        (session["user"],)
    )

    user = cursor.fetchone()

    if user:

        cursor.execute(
            "DELETE FROM watchlist WHERE email=? AND movie=?",
            (user[0], movie)
        )

    conn.commit()
    conn.close()

    return redirect("/watchlist")

@app.route("/movie/<title>")
def movie_details(title):

    movie = movies_df[movies_df["title"] == title]

    if movie.empty:
        return "Movie not found"

    movie = movie.iloc[0]

    recommendations = recommend(title)

    return render_template(
        "details.html",
        movie=movie,
        recommendations=recommendations
    )
@app.route("/search")
def search():

    query = request.args.get("q", "")

    result = movies_df[
        movies_df["title"].str.contains(
            query,
            case=False,
            na=False
        )
    ]

    return render_template(
        "search.html",
        movies=result.to_dict("records"),
        query=query
    )


@app.route("/genre/<genre>")
def genre(genre):

    result = movies_df[
        movies_df["genre"] == genre
    ]

    return render_template(
        "search.html",
        movies=result.to_dict("records"),
        query=genre
    )

@app.route("/top-rated")
def top_rated():

    result = movies_df.sort_values(
        by="rating",
        ascending=False
    )

    return render_template(
        "search.html",
        movies=result.to_dict("records"),
        query="Top Rated"
    )

@app.route("/continue")
def continue_watch():

    result = movies_df[
        movies_df["continue"] > 0
    ]

    return render_template(
        "search.html",
        movies=result.to_dict("records"),
        query="Continue Watching"
    )

@app.route("/favorites")
def favorites():

    result = movies_df[
        movies_df["favorite"] == 1
    ]

    return render_template(
        "search.html",
        movies=result.to_dict("records"),
        query="Favorites"
    )
@app.route("/admin")
def admin():

    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    users=cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM watchlist")
    watchlist=cursor.fetchone()[0]

    movies=len(movies_df)

    conn.close()

    return render_template(
        "admin.html",
        total_movies=movies,
        total_users=users,
        total_watchlist=watchlist
    )
@app.route("/favorite/<movie>")
def favorite(movie):

    if "user" not in session:

        return redirect("/login")

    conn=sqlite3.connect("users.db")

    cursor=conn.cursor()

    cursor.execute(
        "SELECT email FROM users WHERE fullname=?",
        (session["user"],)
    )

    email=cursor.fetchone()[0]

    cursor.execute(
        "INSERT INTO favorites(email,movie) VALUES(?,?)",
        (email,movie)
    )

    conn.commit()

    conn.close()

    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)