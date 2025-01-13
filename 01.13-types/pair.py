class Pair:
    """ A pair of elements """

    def __init__(self, first, second):
        # NOTE: This tells the interpreter how to construct a value of type
        #       Pair. To create a pair, we must pass a "first" argument and a
        #       "second" argument, which will then be assigned to the
        #       attributes "self.first" and "self.second".

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


# This makes pair a reference to an object of type Pair containing the first
#  attribute "hello" and the second attribute "world":
pair = Pair("hello", "world")


def swap(pair):
    """
    Swap the elements of a pair.

    :param pair: A pair of elements
    :return: A new pair with the elements swapped
    """
    return Pair(pair.second, pair.first)
