from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)

# create a route decorator (this is how it called!)
@app.route("/")
def index():
    first_name = "fll"
    return render_template("index.html", first_name=first_name)

@app.route("/header")
def base_bar():
    return render_template("header.html")

@app.route('/user/<name>')
def user(name):
    #return f"hello, {name}"
    return render_template("user.html", name=name)

@app.route("/contact")
def contact():
    return render_template("contact.html")

# invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404