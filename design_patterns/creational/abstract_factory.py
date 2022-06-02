class PetStore:
    """PetStore houses our Abstract Factory"""
    def __init__(self, pet_factory=None):
        """pet_factory is our Abstract Factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the object returned"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        print(f"Our pet is {pet}")
        print(f"Our pet says hello as {pet.speak()}")
        print(f"Its food is {pet_food}")


class DogFactory:
    """Concrete factory"""
    def get_pet(self):
        """Returns a Dog object"""
        return Dog()

    def get_food(self):
        """Returns a Dog Food object"""
        return "Dog food"

class Dog:
    """A simple dog class"""
    def __init__(self, name="Default dog name"):
        self._name = name

    def speak(self):
        return "Woof!"


factory = DogFactory()
shop = PetStore(factory)
shop.show_pet()