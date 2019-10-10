from flask import Flask, redirect, url_for, render_template, abort, request
app = Flask(__name__)

@app.route('/')
def root():
    return "<h1>Hello: All</h1> <p>This is default'root' route</p>"

@app.route('/hello/')
def home():
    return "<h1>Hello all :D</h1>"

@app.route('/goodbye/')
def goodbye():
    print request.method
    return "goodbye"

@app.route('/login')
def login():
    user={'name':'John'}
    return render_template('redirect.html', title='loginpage', user=user)

## redirect user to another endpoint using redirect(url_for(/'login'))

@app.route("/private")
def private():
    return redirect(url_for('login'))



@app.errorhandler(404)
def page_not_found(error):
    return "could'nt find the requested page",404

@app.route('/force404')
def force404():
    abort(404)


@app.route('/static-example/img')
def static_example_img():
    start = '<img src="'
    url = url_for('static', filename='vmask.jpg')
    end = '">'
    return start+url+end, 200

## week 4

@app.route("/account", methods=['GET', 'POST'])
def account():
    if request.method =='POST':
        print request.form
        name = request.form["name"]
        return "Hello " + name + "\n posted"
    else:
        print "get called"
        return render_template('form.html', title='new form')

@app.route("/who/<name>")
def who(name):
    return "Hello %s" % name

@app.route("/sum/<int:first>/<int:second>")
def numbers(first,second):
    return "Sum of numbers is : " + str(first+second)
