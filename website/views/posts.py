import operator
from flask import Blueprint, render_template, request, flash, redirect, url_for
from ..models.Post import Post
from ..repository.postsRepository import PostsRepository
from ..repository.postsRepositoryDb import PostsRepositoryDb
from ..repository import postsSeed
import datetime

posts = Blueprint("posts", __name__)
postsRepository = PostsRepository()
postsSeed.seed(postsRepository)
#Uncomment the following lines for the website to work with DB (only index works as intended)
#postsRepository = PostsRepositoryDb()
#postsSeed.seedDb(postsRepository)

@posts.route("/")
def index():
    allPosts = postsRepository.getAllPreviews()
    if isinstance(postsRepository, PostsRepository):
        allPosts.sort(key = operator.attrgetter("created_at"), reverse=True)
    else:
        allPosts.sort(key=lambda item:item['created_at'], reverse=True)
    return render_template("index.html", posts=allPosts)

@posts.route("/create", methods=['GET', 'POST'])
def create():
    tempPost = Post(None, None, None, None, None, None)
    if request.method == "POST":
        idPost = 1
        title = request.form.get('title')
        content = request.form.get('content')
        owner = "Doesn't matter"
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if not title:
            flash('Title cannot be empty', category='error')
            tempPost.content = content
        elif not content:
            tempPost.title = title
            flash('Content cannot be empty', category='error')
        else:
            post = Post(idPost, title, content, owner, date, date)
            postsRepository.create(post)
            flash('Post created!', category='success')
            return redirect(url_for('posts.index'))

    return render_template('create_post.html', post=tempPost)

@posts.route("/<int:idPost>", methods=['GET', 'POST'])
def read(idPost):
    post = postsRepository.findById(idPost)
    
    if post == None:
        flash('Post does not exist.', category='error')
        return redirect(url_for('posts.index'))

    return render_template('read_post.html', post=post)

@posts.route("/edit/<int:idPost>", methods=['GET', 'POST'])
def edit(idPost):
    post = postsRepository.findById(idPost)
    
    if post == None:
        flash('Post does not exist.', category='error')
        return redirect(url_for('posts.index'))

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
            postsRepository.update(post)
            flash('Post edited!', category='success')
            return redirect(url_for('posts.index'))

    return render_template('edit_post.html', post=post)

@posts.route("delete/<int:idPost>")
def delete(idPost):
    post = postsRepository.findById(idPost)

    if post == None:
        flash('Post does not exist.', category='error')
    else:
        postsRepository.delete(post)
        flash('Post deleted!', category='success')

    return redirect(url_for('posts.index'))