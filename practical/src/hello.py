from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello: All</h1><br><h3>its working</h3>"
