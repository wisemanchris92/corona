from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello_world():
    return 'hello weirdos'


if __name__ == '__main__':
    print("server is running on localhost:5000")
    app.run()