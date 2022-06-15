"""
Establishes a one to many relationship between a subject and multiple observers.

Problem - subject needs to be monitored and other observer objects should be notified
when there is a change in the subject.

Solution:
Subject - abstract class, which has an interface that allows operations to attach,
detach and notify the observers.
Concrete subject classes - inherit from Subject abstract class.

Singleton is related to the Observer pattern.
"""


class Subject(object):
    def __init__(self):
        # This where references to all the observers are being kept
        # Note that this is a one-to-many relationship:
        # there will be one subject to be observed by multiple _observers
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except Exception as e:
            print(e)

    # For all the observers in the list
    # Don't notify the observer who is actually updating the temperature
    # Alert the observers!
    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier is not observer:
                observer.update(self)


class Core(Subject):
    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name
        self._temp = 0

    # Getter that gets the core temp
    @property
    def temp(self):
        return self._temp

    # Setter that sets core temp
    @temp.setter
    def temp(self, temp):
        self._temp = temp
        self.notify()


class TempViewer:
    # Alert method that is invoked
    # when the notify() method in a concrete subject is invoked
    def update(self, subject):
        print(f"Temp Viewer:{subject._name}, has temp:{subject._temp}")


c1 = Core("Core_1")
c2 = Core("Core_2")

v1 = TempViewer()
v2 = TempViewer()

# Lets attach the observers to the Core_1
c1.attach(v1)
c1.attach(v2)

# Lets change the temp of the Core_1
c1.temp = 80
c1.temp = 90
