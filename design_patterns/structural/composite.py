"""
Maintains a tree data structure to represent part-whole relationships

Problem - Recursive tree data structure (some elements have sub elements)
Menu > submenu > sub-submenu > ...

Solution:
Component - abstract class
Child - concrete class, inherits from the Component
Composite - concrete class, inherits from the Component.
It maintains Child objects by adding and removing them to and from a tree data structure
"""


class Component(object):
    """Abstract class"""

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Child(Component):
    """Concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # This is where we store the name of the child item
        self.name = args[0]

    def component_function(self):
        # Print the name of the child item
        print(self.name)


class Composite(Component):
    """Concrete class that maintains the tree recursive structure"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]

        # This will keep child items
        self.children = []

    def append_child(self, child):
        """Method to add new child item"""
        self.children.append(child)

    def delete_child(self, child):
        """Method to delete child item"""
        self.children.remove(child)

    def component_function(self):
        # Print the name of the composite object
        print(self.name)

        # Iterate through the child objects and invoke their component function, printing their names
        for i in self.children:
            i.component_function()


# Build a composite submenu_1
sub1 = Composite("submenu_1")

# Create a new child sub menu 11
sub11 = Child("sub_submenu_11")
# Create a new child sub menu 12
sub12 = Child("sub_submenu_12")

# Add sub_submenu_11, sub_submenu_12 to submenu_1
sub1.append_child(sub11)
sub1.append_child(sub12)

# Build a top-level composite menu
top = Composite("top_menu")

# Build a submenu_2 that is not a composite
sub2 = Child("submenu_2")

# Add the composite submenu_1 to the top-level composite menu
top.append_child(sub1)

# Add the plain submenu 2 to the top-level composite menu
top.append_child(sub2)

top.component_function()
