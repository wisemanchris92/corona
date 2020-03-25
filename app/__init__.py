from flask import Flask


app = Flask(__name__)


from app import routes, errors


# if __name__ == '__main__':
#     print("server is running on localhost:5000")
#     app.run()



