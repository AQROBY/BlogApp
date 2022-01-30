from flask import Blueprint, render_template
from .models import Post
from .repository import repository

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/index")
def index():
    content = ["Alex", "Mariana"]
    x = repository()
    
    return render_template("index.html", content=content)