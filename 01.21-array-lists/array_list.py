class List:
    """ An ordered collection of elements """

    def __init__(self):
        # NOTE: Since an array has fixed length, we have to allocate space for
        #       more elements than we actually need, and we must distinguish
        #       between the number of elements in the list and the number of
        #       available spaces for elements in the array.

        # The length of the backing array:
        self.capacity = 4

        # NOTE: Unlike languages like C or Java, Python does not expose true
        #       arrays to programmers, but we can pretend that a list is an
        #       array: we'll create a list that contains only Nones, and then
        #       avoid using any list operations (e.g., append or extend).

        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this list:
        self.size = 0


def get(lst, idx):
    # NOTE: Since the address of an element can be computed based on its index,
    #       there is now no need to traverse all previous elements in order to
    #       access an element in the middle of the list.
    #
    # Return the element at the given idx in the array.
    pass


def set(lst, idx, value):
    # Set the element at the given idx in the array to the given value.
    pass


def add(lst, idx, value):
    # NOTE: Since arrays have fixed size, if we need space for more elements,
    #       we have to create a completely new, larger array. Rather than just
    #       making space for one more element, we instead make space for twice
    #       as many elements; *some* additions will require us to increase the
    #       capacity, but *most* additions will find that we already have
    #       enough space: on average, the "amortized" complexity of adding
    #       elements can ignore the complexity of increasing the capacity.
    #
    # If the size is equal to the capacity, then:
    #     Set the capacity to capacity * 2.
    #     Create a new array of that capacity.
    #     (copy the elements from the old array into the new array)
    #     Set the array to the new array.
    #
    # NOTE: In order to preserve the property that list indices are the same as
    #       array indices, whenever we add to the list, we have to shift all
    #       elements after that index "down" in the array.
    #
    # For i from the size to the given idx, do:
    #     Set the element at i in the array to the element at i - 1.
    #
    # Set the element at the given idx in the array to the given value.
    # Increment the size.
    pass


def remove(lst, idx):
    # NOTE: Similarly, when removing, we have to shift all the elements after
    #       that index "up" in the array.
    #
    # For i from the given idx to the size - 1, do:
    #     Set the element at i in the array to the element at i + 1.
    #
    # Decrement the size.
    pass
