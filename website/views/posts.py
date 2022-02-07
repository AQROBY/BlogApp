import re
from flask import Blueprint, render_template, request, flash, redirect, url_for
import flask
from flask.helpers import url_for
from flask.wrappers import Request
from ..models.Post import Post
from ..repository.repository import Repository
import datetime

posts = Blueprint("posts", __name__)
repository = Repository()
postex = Post("Title","This is the content",11111, 12312312)
text = "Text textText textText textText textText textText textText textText textText textText textText textText textText text \
    Text textText textText textText textText textText textText textText textText textText textText textText textText text"
postex1 = Post("This is an article", text, 11111, 12312312)
repository.save(postex)
repository.save(postex1)

@posts.route("/")
def starting_url():
    return flask.redirect("/posts")

@posts.route("/posts")
def index():
    posts = repository.findAll()
    return render_template("index.html", posts=posts)

@posts.route("/create", methods=['GET', 'POST'])
def create_post():
    tempPost = Post(None, None, None, None)
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if not title:
            flash('Title cannot be empty', category='error')
            tempPost.content = content
        elif not content:
            tempPost.title = title
            flash('Content cannot be empty', category='error')
        else:
            post = Post(title, content, date, date)
            repository.save(post)
            flash('Post created!', category='success')
            return redirect(url_for('posts.index'))

    return render_template('create_post.html', post=tempPost)

@posts.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit_post(id):
    post = repository.findById(id)
    
    if post == None:
        flash('Post does not exist.', category='error')

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
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
            return redirect(url_for('posts.index'))

    return render_template('edit_post.html', post=post)

@posts.route("delete/<int:id>")
def delete_post(id):
    post = repository.findById(id)

    if post == None:
        flash('Post does not exist.', category='error')
    else:
        repository.delete(post)
        flash('Post deleted!', category='success')

    return redirect(url_for('posts.index'))