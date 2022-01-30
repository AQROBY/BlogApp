from flask import Blueprint, render_template
from .models.Post import Post

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/index")
def index():
    x = Post(1, "Post 1", "This is a post", "Marian", "01-02-2020", "01-02-2020")
    y = Post(2, "Post 2", "This is another post", "Ion", "07-02-2021", "07-02-2021")
    li = [x, y]
    
    return render_template("index.html", content=li)