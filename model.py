# IMPORTS
from storage import add_entry, edit_entry, find_entry


# CLASSES
class Entity:
    fields = NotImplemented  # Needs to be overwritten in the subclasses
    entity_type = NotImplemented

    # Magic methods
    def __init__(self, id_: str) -> None:
        """
        Initialisation method for the abstract `Entity` class.
        """

        if id_ is not None:
            # Get the data of this entity from the database
            record = find_entry(entity_type, id_)  # Table name is the entity type and primary key is `id_`
    
            # Set the attribute values
            for key, value in record.items():
                setattr(self, key, value)

        # Also save the PK as an attribute
        self._id = id_  # We want this to be pseudo-private

    def __repr__(self) -> str:
        return f"{self.__name__}({self._id})"  # Will be overwritten in subclasses

    def __str__(self) -> str:
        return __repr__(self)  # Will be overwritten in subclasses

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
            add_entry(entity_type, data_dict)
        else:  # The entry already exists
            edit_entry(entity_type, self._id, data_dict)

    def to_dict(self) -> dict:
        """
        Converts the entity's attributes into a dictionary.
        Note this EXCLUDES the ID that is provided to this object.
        """

        data_dict = {}
        for field in fields:
            data_dict[field] = getattr(self, field)

        return data_dict

    def validate(self):
        """
        Validates the attribute values.
        """

        # Todo: add; do this after fields have been 

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
            setattr(obj, key, value)

        # Return the new object
        return obj


# TODO: ADD OTHER CLASSES
