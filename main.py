import helper
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")  # reagieren auf url?
def index():
    todos = helper.get_all()
    return render_template("index.html", todos=todos)
    # Import von items nach index


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text")
    date = request.form.get("date")
    helper.add(text, date)
    return redirect(url_for("index"))


@app.route("/update/<int:index>")
def update(index):
    helper.update(index)
    return redirect(url_for("index"))


@app.route("/delete")
def delete():
    helper.delete()
    return redirect(url_for("index"))
