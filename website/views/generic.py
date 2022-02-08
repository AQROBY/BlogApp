from flask import Blueprint, render_template, request, flash, redirect, url_for
import flask

generic = Blueprint("generic", __name__)

@generic.route("/")
def starting_url():
    return flask.redirect("/posts")
