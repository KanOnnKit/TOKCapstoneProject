import validate as valid

class Field:
    def __init__ (self, name: str, lable: str, value: str):
        self.name= name
        self.label= label
        
    def __repr__(self):
        return (
            f'{self.__class__.__name__}('
            f'name="{self.name}",'
            f'label="{self.label}"'
            ')'
        )
        
class IntegerField(Field):
   def __init__(self, name: str, label: str):
        super().__init__(name, label)

class SelectorField(Field):
    def __init__(self, name: str, label: str, selections):
        super().__init__(name, label)
        self.__selections= None

class StringField(Field):
    def __init__(self, name: str, label: str):
        super().__init__(name, label)

class DateField(Field):
    def __init__(self, name: str, label: str):
        super().__init__(name, label)

