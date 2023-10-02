from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory
from PyDictionary import PyDictionary
from random import choice

app = Flask(__name__, static_url_path="/static")
app.secret_key = "your_secret_key"  # Set a secret key for session management
dictionary = PyDictionary()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def sign_in():
    if request.method == 'POST':
        session["user_name"] = request.form["user_name"]
        return redirect(url_for('index'))
    return render_template("login.html")

@app.route("/logout")
def logout():
    # remove the username from the session if it's there
    session.pop("user_name", None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)