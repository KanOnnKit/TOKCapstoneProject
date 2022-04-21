# IMPORTS
from flask import Flask, render_template, request, abort, redirect, url_for

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
    allowed_page_types = {None, "activity", "cca"}  # Use a set for O(1) membership test

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
            # Get the form data
            form = dict(request.form)
            form_keys = form.keys()  # We will compare this with needed keys later
            
            # Handle data in different cases
            if requested_page_type == "activity":
                # Check if all needed parameters are present
                if form_keys == Activity.fields.keys():  # Todo: does this work?
                    # Create new CCA object using the data
                    activityObj = Activity.from_dict(form)

                    # Save the object
                    activityObj.save()
                else:
                    abort(400)  # Todo: currently this raises a 400 Invalid Method error; should we show error instead?
            else:  # The page type has to be "cca"
                # Check if all needed parameters are present
                if form_keys == CCA.fields.keys():  # `CCA.fields` is a set
                    # Create new CCA object using the data
                    ccaObj = CCA.from_dict(form)

                    # Save the object
                    ccaObj.save()
                else:
                    abort(400)  # Todo: currently this raises a 400 Invalid Method error; should we show error instead?

            # Return acknowledgement
            return render_template("confirm.html", data=form)  # Todo: confirm format


@app.route("/view", methods=["GET", "POST"])
def view():
    """
    Page allowing user to see the details of an activity, a CCA, or a class.
    """
    
    # Constants
    allowed_page_types = {None, "activity", "cca", "class", "student"}  # Use a set for O(1) membership test

    # Get the requested page type
    requested_page_type = request.args.get("type", None)

    # Check if the requested page type exists
    if requested_page_type not in allowed_page_types:
        abort(404)  # Todo: add 404 page?

    # Handle different page methods
    if request.method == "GET":
        if requested_page_type is None:
            return render_template("view.html")
        else:
            return render_template("view.html", type=requested_page_type)
            
    else:  # POST
        if requested_page_type is None:
            # Not allowed; return 405 error
            abort(405)

        else:
            # Try and get the ID
            id_ = request.args.get("id", None)

            # Handle different cases depending on whether the ID is present
            if id_ is None:
                return render_template("view.html", type=requested_page_type)
            else:
                # Todo handle data getting

        # Return page request
        return render_page_template("view.html", type=requested_page_type, data_dict)

@app.route("/edit")
def edit():
    """
    Page allowing user to see the details of an activity, a CCA, or a class.
    """
    
    # Constants
    allowed_page_types = {None, "activity", "cca", "student"}  # Use a set for O(1) membership test

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
            # Get the name from the form
            name = request.form.get("name", None)

            # Ensure that a name was passed in
            if name is None:
                abort(400)  # 400 bad request
            else:
                # Get the ID based off the name
                id_ = get_id_from_name(name, requested_page_type)

                # Redirect to correct page
                return redirect(url_for("edit", type=request_page_type, id=id_))  # Todo check if this is correct
        else:
            # Todo add

        # Return acknowledgement
        return render_template("confirm.html", data=form)  # Todo: confirm format


# MAIN CODE
if __name__ == "__main__":
    app.run("0.0.0.0")
