import os

from flask import Flask, app, render_template, request
from palindrome_fabari.phrase import Phrase

def full_title(page_title):
    base_title = "Learn Enough Python Sample App"
    if page_title:
        return f"{base_title} | {page_title}"
    else:
        return base_title

def create_app(test_config=None):
    """Create and configure the app."""
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        # Load the instance config, if it exists, when not testing.
        app.config.from_pyfile("config.py", silent=True)
    else:
        # Load the test config if passed in.
        app.config.from_mapping(test_config)
    # Ensure the instance folder exists.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.add_template_global(full_title)
    
    @app.route("/")
    def index():
        return render_template("index.html", page_title="Home")
    
    @app.route("/about")
    def about():
        return render_template("about.html", page_title="About")
    
    @app.route("/palindrome")
    def palindrome():
        return render_template("palindrome.html", page_title="Palindrome Detector")
    
    @app.route("/check", methods=("POST",))
    def check():
        phrase = request.form["phrase"]
        is_palindrome = Phrase(phrase).ispalindrome()
        return render_template("result.html", phrase=phrase, is_palindrome=is_palindrome)
    

    return app
app = create_app()
