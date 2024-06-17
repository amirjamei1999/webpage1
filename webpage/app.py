import os
from flask import Flask, flash, redirect, render_template, request, session, url_for
from cs50 import SQL
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)


db = SQL("sqlite:///database.db")

@app.route("/")
def index():
        return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        number = int(request.form.get("number"))
        email = request.form.get("email")
        message = request.form.get("message")

        if not name:
            print("please enter a valid name")
        if not number:
            print("please enter a valid number")
        if not email:
            print("please enter a valid email")
        if not message:
            print("text area can't be empty")

        db.execute("INSERT INTO users (name, number, email, message) VALUES (?, ?, ?, ?)", name, number, email, message)
        return redirect("/")

    else:
        return render_template("contact.html")

@app.route("/movies")
def movies():
    return render_template("movies.html")



@app.route("/project")
def project():
    return render_template("project.html")
