#IMPORTS
from datetime import datetime

#Validation error to catch any error
class ValidationError(Exception): pass

"""
Validate methods for Fields and Entities
"""
#Ensure that val is integer
def validate_integer(val):
    if isinstance(val, int):
        return True
    return False

#Ensure that curr_option is among the possible_options
def validate_selection(possible_options, curr_option):
    if curr_option in possible_options:
        return True
    return False

#Ensure that val is non-empty
def validate_string(val):
    if len(val)==0:
        return False
    return True

#Ensure that val is a string that follows the ISO8601 format
def validate_date(val):
    try:
        datetime.formisoformat(val)
    except:
        return False
    return True
