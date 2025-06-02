from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# create a Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my secret key"

# create a Form class 
class NamerForm(FlaskForm):
    name = StringField("what is your name", validators=[DataRequired()])
    submit = SubmitField("Submit")


# create a route decorator (this is how it called!)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    name = None
    form = NamerForm()
    #validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('add_user.html',
         name=name, 
         form=form)

# invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


