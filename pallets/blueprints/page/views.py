from flask import Blueprint, render_template


page = Blueprint("page", __name__, template_folder="templates")


@page.route("/")
def home():
    return render_template("home.j2")


@page.route("/terms")
def terms():
    return render_template("terms.j2")


@page.route("/privacy")
def privacy():
    return render_template("privacy.j2")
