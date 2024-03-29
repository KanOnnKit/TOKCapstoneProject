# IMPORTS
import secrets

from flask import Flask, render_template, request, abort, flash, redirect, url_for

from model import Activity, CCA, Student
from storage import init_db, find_entry, add_relation, remove_relation, get_all_primary_keys
from helpers import get_id_from_name, get_ids_from_names, get_data_from_id
from validation import ValidationError

# SETUP
app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
print("Secret key:", app.secret_key)


# ROUTES
@app.route("/")
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
        abort(404)

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

            # Get the form keys
            form_keys = form.keys()  # We will compare this with needed keys later

            # Handle data in different cases
            try:
                if requested_page_type == "activity":
                    # Check if all needed parameters are present
                    if form_keys == Activity.fields.keys():
                        # Create new CCA object using the data
                        activity_obj = Activity.from_dict(form)

                        # Save the object
                        activity_obj.save()
                    else:
                        abort(400)
                else:  # The page type has to be "cca"
                    # Check if all needed parameters are present
                    if form_keys == CCA.fields.keys():  # `CCA.fields` is a set
                        # Create new CCA object using the data
                        cca_obj = CCA.from_dict(form)

                        # Save the object
                        cca_obj.save()
                    else:
                        abort(400)
            except ValidationError:
                abort(400)

            # Return acknowledgement
            return render_template("confirm.html")


@app.route("/view", methods=["GET", "POST"])
def view():
    """
    Page allowing user to see the details of an activity, a CCA, or a class.
    """

    # Constants
    allowed_page_types = {None, "activity", "cca", "class", "student"}  # Use a set for O(1) membership test

    # Get the requested page type and the ID of the entity
    requested_page_type = request.args.get("type", None)
    id_ = request.args.get("id", None)

    # Check if the requested page type exists
    if requested_page_type not in allowed_page_types:
        abort(404)

    # Handle different page methods
    if request.method == "GET":
        if requested_page_type is not None and id_ is not None:
            # Get the data from the correct ID and type
            data = {}
            try:
                data = get_data_from_id(id_, requested_page_type)
            except KeyError:
                abort(404)
            except ValidationError:
                return redirect(url_for("view"))  # Todo: this should also have context of the validation error

            # Show attributed entities if the requested page type is "class"
            if requested_page_type == "class":  # Note: the implementation below isn't particularly efficient. Oh well
                # Get all students' IDs
                all_student_ids = get_all_primary_keys("student")

                # Get students with the required class
                student_names = []

                for student_id in all_student_ids:
                    record = find_entry("student", "id", student_id)[0]  # Should be unique PK
                    if record["id"] == id_:  # Match class ID
                        student_names.append(record["name"])

                # Add student names to the data dictionary
                data["student_names"] = student_names

            # Return page request
            return render_template("view.html", type=requested_page_type, data_dict=data)

        elif requested_page_type is not None:
            return render_template("view.html", type=requested_page_type)

        else:
            return render_template("view.html")

    else:  # POST
        if requested_page_type is None:
            # Not allowed; return 405 error
            abort(405)

        else:
            # Try and get the name
            name = request.form.get("name", None)

            # Handle different cases depending on whether the name is present
            if name is None:
                return render_template("view.html", type=requested_page_type)
            else:
                # Get the ID based on the name and page type
                id_ = get_id_from_name(name, requested_page_type)

                # Check if an actual ID was returned
                if id_ is None:
                    flash(f"Unknown name '{name}'. Did you enter it correctly?")

                # Redirect to correct page
                return redirect(url_for("view", type=requested_page_type, id=id_))  # Todo check if this is correct


@app.route("/edit", methods=["GET", "POST"])
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
        abort(404)

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
                if requested_page_type == "activity":
                    # Get associated students' IDs
                    records = find_entry("studentactivity", "activity_id", id_)

                    # Get the names of said students
                    student_names = []
                    for record in records:

                        # This code is not particularly efficient. oh well
                        student_obj = Student(record["student_id"])
                        student_names.append(student_obj.name)

                    # Return request
                    return render_template("edit.html", type="activity", associated_students=student_names, id=id_)
                elif requested_page_type == "cca":
                    # Get associated students' IDs
                    records = find_entry("studentcca", "cca_id", id_)

                    # Get the names of said students
                    student_names = []
                    for record in records:
                        # This code is not particularly efficient. oh well
                        student_obj = Student(record["student_id"])
                        student_names.append(student_obj.name)

                    # Return request
                    return render_template("edit.html", type="cca", associated_students=student_names, id=id_)
                else:  # Should be "student"
                    # Get CCA records and activity records
                    cca_records = find_entry("studentcca", "student_id", id_)
                    activity_records = find_entry("studentactivity", "student_id", id_)

                    # Get the names of the CCAs
                    cca_names = []
                    for record in cca_records:
                        cca_obj = CCA(record["cca_id"])
                        cca_names.append(cca_obj.name)

                    activity_names = []
                    for record in activity_records:
                        activity_obj = Activity(record["activity_id"])
                        activity_names.append(activity_obj.name)

                    # Return request
                    return render_template("edit.html", type="student", associated_ccas=cca_names,
                                           associated_activities=activity_names, id=id_)

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

                # Check if an actual ID was returned
                if id_ is None:
                    flash(f"Unknown name '{name}'. Did you enter it correctly?")

                # Redirect to correct page
                return redirect(url_for("edit", type=requested_page_type, id=id_))  # Todo check if this is correct

        else:
            # Handle changes made to the models
            # Todo: apply D.R.Y. principle to below code
            if requested_page_type == "activity":
                # We expect the request form to contain the `associated_students` key
                associated_students = request.form.get("associated_students", None)

                if associated_students is None:
                    abort(400)  # Bad request

                # Process the associated students
                associated_students = set(associated_students.splitlines())

                try:
                    associated_students.remove("")
                except KeyError:
                    pass

                # Get the IDs of the associated students' names
                new_associated_ids = set(get_ids_from_names(list(associated_students), "student").values())

                # Get the existing IDs of the associated students
                records = find_entry("studentactivity", "activity_id", id_)
                old_associated_ids = set([record["student_id"] for record in records])

                # Compute the symmetric set difference to see what changed
                changed_ids = old_associated_ids.symmetric_difference(new_associated_ids)

                # Determine if it was an "add" or a "remove"
                for changed_id in changed_ids:
                    if changed_id in old_associated_ids:
                        # The ID was removed
                        remove_relation("studentactivity", {"student_id": changed_id, "activity_id": id_})
                    else:
                        # The ID was added
                        # Todo: future work - allow adding category, role etc
                        add_relation("studentactivity",
                                     {
                                         "student_id": changed_id, "activity_id": id_, "category": "A",
                                         "role": "Participant", "award": "Award", "hours": 123
                                     }
                                     )

            elif requested_page_type == "cca":
                # We expect the request form to contain the `associated_students` key
                associated_students = request.form.get("associated_students", None)

                if associated_students is None:
                    abort(400)  # Bad request

                # Process the associated students
                associated_students = set(associated_students.splitlines())

                try:
                    associated_students.remove("")
                except KeyError:
                    pass

                # Get the IDs of the associated students' names
                new_associated_ids = set(get_ids_from_names(list(associated_students), "student").values())

                # Get the existing IDs of the associated students
                records = find_entry("studentcca", "cca_id", id_)
                old_associated_ids = set([record["student_id"] for record in records])

                # Compute the symmetric set difference to see what changed
                changed_ids = old_associated_ids.symmetric_difference(new_associated_ids)

                # Determine if it was an "add" or a "remove"
                for changed_id in changed_ids:
                    if changed_id in old_associated_ids:
                        # The ID was removed
                        remove_relation("studentcca", {"student_id": changed_id, "cca_id": id_})
                    else:
                        # The ID was added
                        # Todo: future work - allow adding category, role etc
                        add_relation("studentcca", {"student_id": changed_id, "cca_id": id_, "role": "Participant"})

            else:  # Page type is student
                # We expect the request form to contain the `associated_ccas` and `associated_activities` keys
                associated_ccas = request.form.get("associated_ccas", None)
                associated_activities = request.form.get("associated_activities", None)

                if associated_ccas is None or associated_activities is None:
                    abort(400)  # Bad request

                # Process the associated CCAs and activities
                associated_ccas = set(associated_ccas.splitlines())
                associated_activities = set(associated_activities.splitlines())

                try:
                    associated_ccas.remove("")
                except KeyError:
                    pass

                try:
                    associated_activities.remove("")
                except KeyError:
                    pass

                # Get the IDs of the associated entities' names
                new_associated_cca_ids = set(get_ids_from_names(list(associated_ccas), "cca").values())
                new_associated_activity_ids = set(get_ids_from_names(list(associated_activities), "activity").values())

                # Get the existing IDs of the associated students
                records = find_entry("studentcca", "student_id", id_)
                old_associated_cca_ids = set([record["cca_id"] for record in records])

                records = find_entry("studentactivity", "student_id", id_)
                old_associated_activity_ids = set([record["activity_id"] for record in records])

                # Compute the symmetric set difference to see what changed
                changed_cca_ids = old_associated_cca_ids.symmetric_difference(new_associated_cca_ids)
                changed_activity_ids = old_associated_activity_ids.symmetric_difference(new_associated_activity_ids)

                # Determine if it was an "add" or a "remove"
                for changed_id in changed_cca_ids:
                    if changed_id in old_associated_cca_ids:
                        # The ID was removed
                        remove_relation("studentcca", {"student_id": changed_id, "cca_id": id_})
                    else:
                        # The ID was added
                        # Todo: future work - allow adding category, role etc
                        add_relation("studentcca", {"student_id": changed_id, "cca_id": id_, "role": "Participant"})

                for changed_id in changed_activity_ids:
                    if changed_id in old_associated_activity_ids:
                        # The ID was removed
                        remove_relation("studentactivity", {"student_id": changed_id, "activity_id": id_})
                    else:
                        # The ID was added
                        # Todo: future work - allow adding category, role etc
                        add_relation("studentactivity",
                                     {
                                         "student_id": changed_id, "activity_id": id_, "category": "A",
                                         "role": "Participant", "award": "Award", "hours": 123
                                     }
                                     )

            # Return acknowledgement
            return render_template("confirm.html")


# MAIN CODE
if __name__ == "__main__":
    # Initialize database
    init_db()

    # Run the app
    app.run("0.0.0.0")
