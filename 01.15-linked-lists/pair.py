# NOTE: A pair is very similar to a list, in that pairs are also finite,
#       ordered collections of elements. The only difference is that pairs can
#       only contain precisely two elements. We could define a "triple" that
#       contains precisely three elements, but then we would just have the same
#       problem for a collection of four elements...

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


# NOTE: ...alternatively, since the elements of a pair may have any type, the
#       second element of a pair could be *another pair*. We can then create
#       arbitrarily large collections by nesting arbitrarily many pairs:
lst = Pair('a', Pair('b', Pair('c', None)))
