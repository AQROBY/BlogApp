from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "hello"

    from .views import posts
    from .views import index

    app.register_blueprint(index.index, url_prefix="/")
    app.register_blueprint(posts.posts, url_prefix="/posts")

    return app