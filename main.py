from flask import Flask, render_template

# flask application instance. this line is foundational in amy Flask app!
# app - pbject is what ties everything together; 
# routes, congifuration, running the server, middleware, bluprints.. 
# __name__ is special python var that represents the name of current module
# Flask uses it to: find static files and templetes based of location of your script
app = Flask(__name__)

@app.route("/")

def main_route():
    return "<h1>letscheck</h1>"

@app.route('/user/<name>')
def user_name(name):
    #return "Hello, {}".format(name)
    #return f"hello, {name}"
    return render_template("user.html", name=name)


