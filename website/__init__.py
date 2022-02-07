from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "hello"

    from .views import posts

    app.register_blueprint(posts.posts, url_prefix="/")

    return app