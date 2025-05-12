from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)

# create a route decorator (this is how it called!)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404