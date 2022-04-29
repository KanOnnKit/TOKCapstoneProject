#IMPORTS
import validate as valid

"""
Class Fields define the different types of field for entities- to be used in model.py.
Has the following fields:
IntegerField, SelectorField, StringField, Datefield.
To validate each fields using validation.py
"""

class Field:
    def __init__ (self, name: str, label: str):
        self.name= name
        self.label= label
        
    def __repr__(self):
        return (
            f'{self.__class__.__name__}('
            f'name="{self.name}",'
            f'label="{self.label}"'
            ')'
        )

    def validate(self, value):
        """Raise error if value does not pass validation"""
        raise NotImplementedError
        
class IntegerField(Field):
    def __init__(self, name: str, label: str):
        super().__init__(name, label)

    def validate(self, value):
        if valid.validate_integer(value) is False:
            raise valid.ValidationError(f"{value} is not a valid int")

class SelectorField(Field):
    def __init__(self, name: str, label: str, selections):
        super().__init__(name, label)
        self.__selections = selections

    def validate(self, selection):
        if valid.validate_selection(self.__selections, selection) is False:
            raise valid.ValidationError(f"{selection} is not in possible selectors.")
            

class StringField(Field):
    def __init__(self, name: str, label: str):
        super().__init__(name, label)

    def validate(self, value):
        if valid.validate_string(value) is False:
            raise valid.ValidationError(f"{value} is an empty string.")
            
class DateField(Field):
    def __init__(self, name: str, label: str):
        super().__init__(name, label)

    def validate (self, date):
        if valid.validate_date(date) is False:
            raise valid.ValidationError(f"Invalid date type: {date}.")

