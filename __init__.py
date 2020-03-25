from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/suckers')
def hello_world():
    return render_template('suckers.html')


if __name__ == '__main__':
    print("server is running on localhost:5000")
    app.run()