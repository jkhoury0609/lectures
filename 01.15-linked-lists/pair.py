# NOTE: Just like a list, a pair is a finite, ordered collection of elements.
#       However, lists must be able to contain arbitrarily many elements, and
#       pairs can only contain exactly two. If we wanted to contain three
#       elements, we could add a third attribute, but then we would just have
#       exactly the same problem with four elements...

class Pair:
    """ A pair of elements """

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __eq__(self, other):
        return (type(other) == type(self)
                and self.first == other.first
                and self.second == other.second)

    def __repr__(self):
        return "Pair(%r, %r)" % (self.first, self.second)

# NOTE: ...instead, since the elements of a pair can have any type, the second
#       element could be *another pair*. We can then contain arbitrarily many
#       elements by nesting arbitrarily many pairs:
lst = Pair('a', Pair('b', Pair('c', None)))
