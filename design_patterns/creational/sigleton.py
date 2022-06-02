class Borg:
    """The Borg design pattern"""
    _shared_data = {}

    def __init__(self):
        self.__dict__ = self._shared_data


class Singleton(Borg):
    """The singleton class"""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)

    def __str__(self):
        return str(self._shared_data)


# Creating singleton object
x = Singleton(HTTP="Hyper Text Transfer Protocol")

# print the object
print(x)

# Creating another singleton object
y = Singleton(SNMP="Simple Network Management Protocol")

# print the object
print(y)
