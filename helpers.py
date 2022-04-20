# IMPORTS
from storage import get_all_primary_keys_and_names


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
    pk_to_names_dict = get_all_primary_keys_and_names(type_)  # This assumes that `type_` is EXACTLY the name of the table

    # Iterate through the dictionary to find the ID match
    for key, value in pk_to_names_dict.items():
        if value == name:
            return key  # This is the ID we are looking for


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
    names = set(names)  # I hope this doesn't override the original list...
    
    # Get the names and primary keys from the table of the appropriate type
    pk_to_names_dict = get_all_primary_keys_and_names(type_)  # This assumes that `type_` is EXACTLY the name of the table

    # Iterate through the dictionary to find the matching IDs
    id_matches = {}
    for key, value in pk_to_names_dict.items():
        if value in names:  # There was a matching name in the set of desired names
            id_matches[value] = key

    # Return the dictionary of ID matches
    return id_matches
