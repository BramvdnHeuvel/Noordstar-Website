from flask import send_from_directory
from src.routes import render

def home():
    """
        Homepage of the website. Here, users get an introduction
        to the website and can see the main part.
    """
    return render('base.html')

def robots():
    """
        Show the `robots.txt` file
    """
    return send_from_directory('static/', 'robots.txt')

def editor():
    """
        Page that lets you edit and preview posts.
    """
    return render('pages/editor.html')
