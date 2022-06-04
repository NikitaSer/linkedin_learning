"""
Allows users to add new features to the existing objects
without changing their structures

Problem - add new feature to an existing object.
Dynamic changes.
Not using subclasses.

Solution - define custom decorator.

Adapter, composite and strategy patters are related.
"""

from functools import wraps


def make_blink(function):
    """Defines a decorator"""

    # This makes the decorator transparent in terms of its name and docstring
    @wraps(function)

    # Defines the inner function
    def decorator():
        # Grab the return value of the function being decorated
        ret = function()

        # Add new functionality to the function being decorated
        return f"<blink>{ret}</blink>"

    return decorator


# Apply the decorator
@make_blink
def hello():
    """Original function"""
    return "Hello"


# Check the result of decorating
print(hello())

# Check that the function name is the original
print(hello.__name__)

# Check that the docstring is from the original function
print(hello.__doc__)
