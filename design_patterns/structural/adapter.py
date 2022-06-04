"""
Converts the interface of a class into another one a client is expecting

Problem - incompatible interfaces between a client and a server

Solution - translate the method names between the client and the server code.

Bridge and Decorator patterns ar related to the Adapter pattern.
"""


class Korean:
    """Korean speaker"""

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong"


class British:
    """English speaker"""

    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello"


class Adapter:
    """This changes the generic method name to individualized method names"""

    def __init__(self, object, **adapted_method):
        """Change the name of the method"""
        self._object = object

        # Add a new dictionary item that establishes the mapping between the generic method name: speak() and the
        # concrete method For example, speak() will be translated to speak_korean() if the mapping says so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of the attributes"""
        return getattr(self._object, attr)


# List to store speaker objects
objects = []

# Create a Korean and British objects
k = Korean()
b = British()

objects.append(Adapter(k, speak=k.speak_korean))
objects.append(Adapter(b, speak=b.speak_english))

for obj in objects:
    print(f"{obj.name} says {obj.speak()}")
