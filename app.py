from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!-Hi'

@app.route('/test')
def hello_test():
    return 'Hello, from test'
