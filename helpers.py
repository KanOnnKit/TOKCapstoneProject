# IMPORTS
from storage import get_all_primary_keys_and_names
from model import Activity, CCA, Class, Student, Subject


# FUNCTIONS
def get_id_from_name(name: str, type_: str) -> str:
    """
    Gets the ID (i.e. primary key) of the name of the specified type `type_`.
    """
    
    # Constants
    allowed_page_types = ["activity", "cca", "class", "student"]

    # Check if the requested page type exists
    if type_ not in allowed_page_types:
        raise ValueError("Invalid page type")

    # Get the names and primary keys from the table of the appropriate type
    pk_to_names_records = get_all_primary_keys_and_names(type_)  # This assumes that `type_` is EXACTLY the name of the table

    # Iterate through the dictionary to find the ID match
    for record in pk_to_names_records:
        if record["name"].upper() == name.upper():
            return record["id"]  # This is the ID we are looking for


def get_ids_from_names(names: list, type_: str) -> dict:
    """
    Returns a DICTIONARY of name-to-id matches.
    """
    
    # Constants
    allowed_page_types = ["activity", "cca", "class", "student"]

    # Check if the requested page type exists
    if type_ not in allowed_page_types:
        raise ValueError("Invalid page type")

    # Convert the `names` list into a set for O(1) membership checking
    names = set([name.upper() for name in names])
    
    # Get the names and primary keys from the table of the appropriate type
    pk_to_names_records = get_all_primary_keys_and_names(type_)  # This assumes that `type_` is EXACTLY the name of the table

    # Iterate through the dictionary to find the matching IDs
    id_matches = {}
    for record in pk_to_names_records:
        if record["name"].upper() in names:  # There was a matching name in the set of desired names
            id_matches[record["name"]] = record["id"]

    # Return the dictionary of ID matches
    return id_matches


def get_data_from_id(id_: str, type_) -> dict:
    """
    Returns the data of the specific entity with the specified ID and with the correct type.
    Raises `ValueError` if the `type_` is invalid.
    """

    # Constants
    type_to_model = {  # Helps convert a type string into the model class
        "activity": Activity,
        "cca": CCA,
        "class": Class,
        "student": Student,
        "subject": Subject
    }
    
    # Validate the `type_`
    if type_ not in type_to_model.keys():
        raise ValueError(f"Invalid entity type {type_}")

    # Retrieve data
    model = type_to_model[type_]  # Get the class of that specific type
    obj = model(id_)  # Call constructor of model
    return obj.to_dict()  # Return data as dictionary
