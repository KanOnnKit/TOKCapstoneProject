# FUNCTIONS
def get_id_from_name(name, type_):
    # Constants
    allowed_page_types = ["activity", "cca", "class", "student"]

    # Check if the requested page type exists
    if type_ not in allowed_page_types:
        raise ValueError("Invalid type")

    # Todo: add


def get_ids_from_names(names, type_):
    # Constants
    allowed_page_types = ["activity", "cca", "class", "student"]

    # Check if the requested page type exists
    if type_ not in allowed_page_types:
        raise ValueError("Invalid type")

    # Get IDs
    ids = []
    for name in names
        ids.append(get_name_from_id(name))

    # Return the list of IDs
    return ids
