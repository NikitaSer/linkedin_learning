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