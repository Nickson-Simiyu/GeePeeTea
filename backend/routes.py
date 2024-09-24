from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template("index.html")

@main.route('/next')
def back():
    return render_template("parent/register-parent.html")