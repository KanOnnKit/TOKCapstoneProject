# IMPORTS
from flask import Flask, render_template, request

# Other imports here

# SETUP
app = Flask(__name__)

# ROUTES
@app.route("/")
def welcome():
    return "Welcome page"

@app.route("/index")
def index():
    return "Index page"

@app.route("/add")
def add():
    return "Add page"

@app.route("/view")
def view():
    return "View page"

@app.route("/edit")
def edit():
    return "Edit page"

@app.route("/api/name_id_lookup")
def api_name_id_lookup():
    return "API Name ID Lookup Page"

    
# MAIN CODE
app.run("0.0.0.0")
