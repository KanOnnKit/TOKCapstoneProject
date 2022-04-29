from datetime import datetime

class ValidationError(Exception):
    pass

def validate_integer(val):
    if isinstance(val, int):
        return True
    return False

def validate_selection(possible_options, curr_option):
    if curr_option in possible_options:
        return True
    return False

def validate_string(val):
    if len(val)==0:
        return False
    return True

def validate_date(val):
    try:
        datetime.fromisoformat(val)
    except ValueError:
        return False
    return True
