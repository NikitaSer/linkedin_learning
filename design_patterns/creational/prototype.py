import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    """Product"""

    def __init__(self):
        self.model = "Swift"
        self.tires = 17
        self.engine = 1.3

    def __str__(self):
        return f"{self.model} | {self.tires} | {self.engine}"


car = Car()
prototype = Prototype()
prototype.register_object("Swift", car)

car_clone = prototype.clone("Swift")

print(car_clone)
