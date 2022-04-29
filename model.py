# IMPORTS
from fields import IntegerField, StringField, SelectorField, DateField
from storage import add_entry, edit_entry, find_entry


# CLASSES
class Entity:
    """
    Abstract class that stores and handles the functions needed by an entity.
    
    This class has two class attributes:
        - fields: the fields that will be shown when displaying to the user. 
                  Is a dictionary mapping field name to field
        - table_name: the table name in the database that contains the data for this entity
    """
    
    fields = NotImplemented  # Needs to be overwritten in the subclasses; contains `Field` objects
    table_name = NotImplemented

    # Magic methods
    def __init__(self, id_: str) -> None:
        """
        Initialisation method for the abstract `Entity` class.

        If the validation fails, raises a `ValidationError`.
        """

        if id_ is not None:
            # Get the data of this entity from the database
            print(self.table_name, id_)
            record = find_entry(self.table_name, "id", int(id_))  # Primary key is `id_`
            print(record)
    
            # Set the attribute values
            for key, value in record.items():
                # Catch ValidationError if necessary
                print(key, value)
                self.fields[key].validate(value)
                
                # Update attribute
                setattr(self, key, value)

        # Also save the PK as an attribute
        self._id = id_  # We want this to be pseudo-private

    def __repr__(self) -> str:
        return f"{self.__name__}({self._id})"  # Will be overwritten in subclasses

    def __str__(self) -> str:
        return self.__repr__()  # Will be overwritten in subclasses

    # Public methods
    def save(self) -> None:
        """
        Save the attributes' values back into the database, using the ID that is (maybe) provided.
        """

        # Get the dictionary of data values
        data_dict = self.to_dict()

        # Update/Create the database entry
        if self._id is None:
            # Create a new entry
            add_entry(self.table_name, data_dict)

        else:  # The entry already exists
            edit_entry(self.table_name, self._id, data_dict)

    def to_dict(self) -> dict:
        """
        Converts the entity"s attributes into a dictionary.
        Note this EXCLUDES the ID that is provided to this object.
        """

        data_dict = {}
        for field in self.fields.keys():
            data_dict[field] = getattr(self, field)

        return data_dict

    def validate(self) -> bool:
        """
        Validates the attribute values. Returns `True` if all valid, `False` otherwise.
        """

        for key in self.fields.keys():
            if not self.fields[key].validate(getattr(self, key)):  # Not valid value
                return False

        return True  # All checks passed
                
    # Class methods
    @classmethod
    def from_dict(cls, dictionary: dict) -> object:
        """
        Initialises an `Entity` object based on the dictionary values.
        This assumes that all the keys are VALID FIELD NAMES of the entity.
        """

        # Create a new object
        obj = cls(None)  # No ID provided

        # Set the attributes of this new entity based on the dictionary
        for key, value in dictionary.items():
            # field = self.fields[key]
            # This will raise validation.ValidationError if validation fails
            # field.validate(value)
            setattr(obj, key, value)

        # Return the new object
        return obj


class Subject(Entity):
    """
    Stubject entity.

    Has the following fields:
        - name: Name of the subject (string, with selections)
        - level: Level of the subject (string, with selections)

    Table name is "subject".
    """

    fields = {
        "name": SelectorField("name", "Name of Subject", {"CLL", "PW", "MATH", "HIST", "PHY", "CHEM", "ML", "TL", "CLB", "GEO", "BENGALESE", "JAPANESE", "HINDI", "BIO", "CLTRANS", "PUNJABI", "FM", "CL", "ECONS", "GP", "ART", "ELIT", "COMP"}),
        "level": SelectorField("level", "Subject Level", {"H1", "H2", "H3"})
    }
    table_name = "subject"


class Student(Entity):
    """
    Student entity.

    Has the following fields:
        - name: Name of the student (string)
        - age: Age of the student (integer)
        - year_enrolled: Year that the student enrolled (integer)
        - graduating_year: Year that the student will graduate (integer)

    Table name is "student".
    """

    fields = {
        "name": StringField("name", "Name of the Student"),
        "age": IntegerField("age", "Student Age"),
        "year_enrolled": IntegerField("year_enrolled", "Year Enrolled"),
        "graduating_year": IntegerField("graduating_year", "Year of Graduation")
    }
    table_name = "student"


class Class(Entity):
    """
    Class entity.

    Has the following fields:
        - name: Class name (string)
        - level: Level of the class (string, with selections)

    Table name is "class"
    """

    fields = {
        "name": StringField("name", "Class Name"),
        "level": SelectorField("level", "Class Level", {"JC1", "JC2"})
    }
    table_name = "class"


class CCA(Entity):
    """
    CCA entity.

    Has one field: name (of the CCA); is a string.
    Table name is "cca"
    """

    fields = {
        "name": StringField("name", "CCA Name")
    }
    table_name = "cca"


class Activity(Entity):
    """
    Activity entity.

    Has the following fields:
        - name: Activity name (string)
        - start_date: Starting date of the activity (date field)
        - end_date: Ending date of the activity (date field)
        - description: Description of the activity (string field)

    Table name is "activity".
    """

    fields = {
        "name": StringField("name", "Activity Name"),
        "start_date": DateField("start_date", "Activity Starting Date"),
        "end_date": DateField("end_date", "Activity Ending Date"),
        "description": StringField("description", "Activity Description")
    }
    table_name = "activity"
