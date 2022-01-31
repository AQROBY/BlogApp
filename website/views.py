from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.helpers import url_for
from .models.Post import Post
from .repository.repository import Repository
import datetime

views = Blueprint("views", __name__)
repository = Repository()

@views.route("/")
@views.route("/index")
def index():
    posts = repository.findAll()
    return render_template("index.html", posts=posts)

@views.route("/create-post", methods=['GET', 'POST'])
def create_post():
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('text')
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if not title:
            flash('Title cannot be empty', category='error')
        elif not content:
            flash('Content cannot be empty', category='error')
        else:
            post = Post(title, content, date, date)
            repository.save(post)
            flash('Post created!', category='success')
            return redirect(url_for('views.index'))

    return render_template('create_post.html')

@views.route("delete-post/<int:id>")
def delete_post(id):
    post = repository.findById(id)

    if post == None:
        flash('Post does not exist.', category='error')
    else:
        repository.delete(post)
        flash('Post deleted!', category='success')

    return redirect(url_for('views.index'))