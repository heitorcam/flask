from flask import Flask, render_template

# Create a Flask instance
app=Flask(__name__)

# Create a route decorator
@app.route("/")

#FILTERS
# lower and upper
# trim
# title
# striptags
# safe


def index():
    first_name = 'Heitor'
    stuff = "This is bold text"

    favorite_pizza = ["Pepperoni","Cheese","Mushroom","Leleca",40]
    return render_template("index.html",
        first_name=first_name,
        stuff=stuff,
        favorite_pizza=favorite_pizza)

#localhost:5000/user/name
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

# Create custom error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error      change
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
