from flask import Blueprint, render_template, request, flash
from .models.Post import Post
from .repository.repository import Repository

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/index")
def index():
    x = Post("Post 1", "This is a post", "Marian", "01-02-2020", "01-02-2020")
    y = Post("Post 2", "This is another post", "Ion", "07-02-2021", "07-02-2021")
    z = Post("Post 2", "This is another post", "Ion", "07-02-2021", "07-02-2021")

    xx = Repository()
    xx.save(x)
    xx.save(y)
    xx.save(z)
    
    return render_template("index.html", content=xx.findAll(), findId=xx.findById(1))

@views.route("/create-post", methods=['GET', 'POST'])
def create_post():
    if request.method == "POST":
        text = request.form.get('text')

        if not text:
            flash('Post cannot be empty', category='error')
        else:
            post = Post()
            flash('Post created!', category='success')
    return render_template('create_post.html')