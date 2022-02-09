from flask import Blueprint, render_template, request, flash, redirect, url_for
import flask

index = Blueprint("index", __name__)

@index.route("/")
def starting_url():
    return flask.redirect("/posts")
