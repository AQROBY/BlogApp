from flask import Blueprint, redirect

index = Blueprint("index", __name__)

@index.route("/")
def starting_url():
    return redirect("/posts")
