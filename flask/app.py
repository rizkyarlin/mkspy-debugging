from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    x = 1
    x += 1
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
