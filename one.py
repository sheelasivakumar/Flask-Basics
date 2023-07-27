# Importing the "Class:Flask" from the module "flask"
# Importing redirect and url_for to redirect the user to a specific function when then are not authorised to enter the one
from flask import Flask, redirect, url_for

# Creating an Instances of the class Flask with the name of the current module
app  = Flask(__name__)

# Decorator to define the route of the functio 
@app.route('/')
def Home():
    return "Hello <h2>Home</h2> page"

@app.route('/<name>')
def welcome(name):
    return f"Welcome! {name}"

@app.route('/edit')
def Admin():
    # Just enter the Function name
    return redirect(url_for("Home"))

if __name__ == "__main__":
    app.run()