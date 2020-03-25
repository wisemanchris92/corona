from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='home')


@app.route('/about')
def about():
    return render_template('about.html', title='about')


# @app.route('/contact')
# def contact():
#     return render_template('contact.html', title='contact')


@app.route('/suckers')
def hello_world():
    return render_template('suckers.html', title='secret')