import re
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.helpers import url_for
from flask.wrappers import Request
from ..models.Post import Post
from ..repository.repository import Repository
import datetime

views = Blueprint("views", __name__)
repository = Repository()

@views.route("/")
@views.route("/index")
def index():
    posts = repository.findAll()
    return render_template("index.html", posts=posts)

@views.route("/create", methods=['GET', 'POST'])
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

@views.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit_post(id):
    post = repository.findById(id)
    
    if post == None:
        flash('Post does not exist.', category='error')

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['text']
        
        if not title:
            flash('Title cannot be empty', category='error')
        elif not content:
            flash('Content cannot be empty', category='error')
        else:
            post.title = title
            post.content = content
            post.modified_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            repository.update(post)
            flash('Post created!', category='success')
            return redirect(url_for('views.index'))

    return render_template('edit_post.html', post=post)

@views.route("delete/<int:id>")
def delete_post(id):
    post = repository.findById(id)

    if post == None:
        flash('Post does not exist.', category='error')
    else:
        repository.delete(post)
        flash('Post deleted!', category='success')

    return redirect(url_for('views.index'))