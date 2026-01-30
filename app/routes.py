from flask import Blueprint, render_template

# Define the "Blueprint"
# 'main' is the internal name, __name__ is the import path
main = Blueprint('main', __name__)

@main.route('/')
def index():
    # This expects a file named 'index.html' in the templates folder
    return render_template('index.html')

@main.route('/health')
def health_check():
    return "ATS System: Online", 200