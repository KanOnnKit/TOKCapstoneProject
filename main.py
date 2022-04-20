# IMPORTS
from flask import Flask, render_template, request, abort

from storage import find_primary_key
from helpers import get_id_from_name, get_ids_from_name

# SETUP
app = Flask(__name__)

# ROUTES
@app.route("/")
def welcome():
    """
    Splash page of the website.
    """
    return render_template("splash.html")


@app.route("/index")
def index():
    """
    Index page of the website, showing user available actions that they can take.
    """
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    """
    Pages to allow user to add new entities.
    """

    # Constants
    allowed_page_types = [None, "cca", "activity"]

    # Get the requested page type
    requested_page_type = request.args.get("type", None)

    # Check if the requested page type exists
    if requested_page_type not in allowed_page_types:
        abort(404)  # Todo: add 404 page?
        
    # Handle different page methods
    if request.method == "GET":
        # Show the page with the correct type
        if requested_page_type is None:
            return render_template("add.html")
        else:
            return render_template("add.html", type=requested_page_type)

    elif request.method == "POST":
        # Check if the page type is `None`
        if requested_page_type is None:
            # Not allowed; return 405 error
            abort(405)
        else:
            # Handle data in different cases
            # Todo: add
            pass


@app.route("/view", methods=["GET", "POST"])
def view():
    # Constants
    allowed_page_types = [None, "activity", "cca", "class", "student"]

    # Get the requested page type
    requested_page_type = request.args.get("type", None)

    # Check if the requested page type exists
    if requested_page_type not in allowed_page_types:
        abort(404)  # Todo: add 404 page?

    # Handle different page methods
    if request.method == "GET":
        if requested_page_type is None:
            return render_page_template("view.html")
        else:
            return render_page_template("view.html", type=requested_page_type)
            
    else:  # POST
        if requested_page_type is None:
            # Not allowed; return 405 error
            abort(405)

        # Generate data dictionary
        # Todo add
        data_dict = {}

        # Return page request
        return render_page_template("view.html", type=requested_page_type, data_dict)

@app.route("/edit")
def edit():
    # Constants
    allowed_page_types = [None, "activity", "cca", "student"]

    # Get the requested page type
    requested_page_type = request.args.get("type", None)

    # Check if the requested page type exists
    if requested_page_type not in allowed_page_types:
        abort(404)  # Todo: add 404 page?

    # Handle different page methods
    if request.method == "GET":
        if requested_page_type is None:
            return render_template("edit.html")
        else:
            # Try and get the ID
            id_ = request.args.get("id", None)

            # Handle different cases depending on whether the ID is present
            if id_ is None:
                return render_template("edit.html", type=requested_page_type)
            else:
                # Todo handle data getting
        
        
    else:  # POST
        if requested_page_type is None:
            # Not allowed; return 405 error
            abort(405)

        # Try and get the ID
        id_ = request.args.get("id", None)

        # Handle different cases depending on whether the ID is present
        if id_ is None:
            # Todo add
        else:
            # Todo add
    
# MAIN CODE
app.run("0.0.0.0")
