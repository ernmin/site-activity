from flask import Blueprint, render_template

search = Blueprint("search", __name__, static_folder="static", template_folder="templates")

@search.route("/")
def search_page():
    return render_template("search.html")