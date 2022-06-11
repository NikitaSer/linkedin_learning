"""
Allows adding new features to the existing class hierarchy without changing it.

Problem - add new operations dynamically to the existing classes with minimal changes.

Solution - new operations to be performed on the various elements of an existing class hierarchy.
"""


class House(object):
    """The class being visited"""
    def accept(self, visitor):
        """
        Interface to accept a visitor
        Triggers the visiting operation
        """
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        # Note that we now have a reference to the HVAC specialist object in the house object!
        print(self, "worked on by", hvac_specialist)

    def work_on_electricity(self, electrician):
        # Note that we now have a reference to the electrician object in the house object!
        print(self, "worked on by", electrician)

    def __str__(self):
        return self.__class__.__name__


class Visitor(object):
    """Abstract visitor"""
    def __str__(self):
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    """Concrete visitor: HVAC specialist"""
    def visit(self, house):
        house.work_on_hvac(self)


class Electircian(Visitor):
    """Concrete visitor: electrician"""
    def visit(self, house):
        house.work_on_electricity(self)


hv = HvacSpecialist()
e = Electircian()

house = House()

# Let the house accept the HVAC specialist and work on the house by invoking the visit() method
house.accept(hv)

# Let the house accept the electrician and work on the house by invoking the visit() method
house.accept(e)
