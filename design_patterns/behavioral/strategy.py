"""
Offers a family of interchangeable algorithms to the client.

Problem - there is a need for dynamically changing the behavior of an object.

Solution - the types module in Python
"""

# Supports the dynamic creation of a new types
import types


class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function=None):
        self.name = "Default Strategy"

        # If a reference to a function is provided, replace the execute() method with the given function
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):  # This gets replaced by another version if another strategy is provided.
        """The default method that prints the name of the strategy being used"""
        print(f"{self.name} is used")


# Replacement method 1
def strategy_one(self):
    print(f"{self.name} is used to execute method 1")


# Replacement method 2
def strategy_two(self):
    print(f"{self.name} is used to execute method 2")


# Lets create our default strategy
s0 = Strategy()

# Lets execute our default strategy
s0.execute()

# Create and test replacements
s1 = Strategy(function=strategy_one)
s1.name = "s1 strategy"
s1.execute()

s2 = Strategy(function=strategy_two)
s2.name = "s2 strategy"
s2.execute()
