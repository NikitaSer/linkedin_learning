"""
Encapsulates object creation. Factory is an object specializing in creating other objects.

Problem - uncertainties in types of objects which you will using eventually in the system.
Decisions to be made at runtime regarding what classes to use.
"""


class Dog:
    """A simple dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:
    """A simple cat class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meaw!"


def get_pet(pet="dog"):
    """The factory methods"""
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]


pet = get_pet(pet="cat")
print(pet._name)
