class Pair:
    """ A pair of elements """

    def __init__(self, first, second):
        # NOTE: This tells the interpreter how to construct a value of type
        #       Pair. To create a pair, we must pass a "first" argument and a
        #       "second" argument, which will then be assigned to the
        #       attributes "self.first" and "self.second", respectively.
        self.first = first
        self.second = second

    def __eq__(self, other):
        # NOTE: This tells the interpreter how to compare two values of type
        #       Pair for equality -- without this method, the interpreter would
        #       default to simply checking whether or not the values were at
        #       the same place in memory, regardless of their attributes:
        return (type(other) == type(self)
                and self.first == other.first
                and self.second == other.second)

    def __repr__(self):
        # NOTE: This tells the interpreter how to convert a value of type Pair
        #       into a string, for example, when printing it out:
        return "Pair(%r, %r)" % (self.first, self.second)


# NOTE: All of the above code merely defines what a Pair ought to look like; it
#       doesn't actually create any values of type Pair. The following actually
#       creates a Pair object, and makes the value pair a reference to that
#       object:
pair = Pair(1, 2)


# NOTE: The above class together with the following function implement a data
#       structure (typically called the "pair" data structure), which in turn
#       implements an abstract data type (also called the "pair" ADT).
def swap(pair):
    """
    Swap the elements of a pair.

    :param pair: A pair of elements
    :return: A new pair with the elements swapped
    """
    return Pair(pair.second, pair.first)
