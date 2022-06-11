"""
Allows a client to have sequential access to the elements of an aggregate object
without exposing its underlying structure.

Problem - the traversal interfaces of an aggregate object getting overcrowded,
for every possible way of iteration.

Solution:
Isolate an interface and traversal features from the aggregate object.
Provide an interface for accessing the elements of an aggregate object.
Keep track on the object being traversed.
Make the aggregate object create an iterator for a client.

Composite design pattern is related to the Iterator.
"""


def count_to(count):
    """Our iterator implementation"""

    # Our list
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    # Our built-in iterator
    # Creates a tuple such as (1, "eins)
    iter = zip(range(count), numbers_in_german)

    # Iterate through our iterable list
    # Extract the German numbers
    # Put them in a generator called number
    for position, number in iter:
        # Returns a generator containing numbers in German
        yield number


for num in count_to(3):
    print(num)
