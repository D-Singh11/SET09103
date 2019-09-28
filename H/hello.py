from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello All'

@app.route('/next')
def next():
    return '<h1>next</h1>'

@app.route('/home')
def home():
    return '<b align="right">This is flask</b>'
app.run(debug=True)

