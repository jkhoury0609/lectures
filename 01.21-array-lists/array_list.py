class List:
    """ An ordered collection of elements """

    def __init__(self):
        # NOTE: Since an array has fixed length, we have to allocate space for
        #       more elements than we actually need. We must distinguish
        #       between the number of elements in the list and the number of
        #       available spaces in the array.

        # The length of the backing array:
        self.capacity = 4

        # NOTE: Unlike languages like C or Java, Python does not have true
        #       arrays, but for the sake of illustration we can pretend that a
        #       list is an array: we'll create a list that contains only Nones,
        #       and then avoid using any of the list operations (e.g., append).

        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this list:
        self.size = 0


def get(lst, idx):
    # Return the element in the array at the given idx.
    pass


def set(lst, idx, value):
    # Set the element in the array at the given idx to the given value.
    pass


def add(lst, idx, value):
    # NOTE: Since arrays have fixed size, if we need space for more elements,
    #       we have to create a completely new, larger array. Rather than just
    #       making space for one more element, we instead make space for twice
    #       as many elements; *some* additions will require us to increase the
    #       capacity, but *most* additions will find that we already have
    #       enough space: on average, the "amortized" complexity can ignore the
    #       complexity of increasing the capacity.
    #
    # If the size is equal to the capacity, then:
    #     Set the capacity to the capacity * 2.
    #     Create a new array of that capacity.
    #     (copy the elements of the old array into the new array)
    #     Set the old array to the new array.
    #
    # NOTE: In order to preserve the property that list indices are the same as
    #       array indices, when adding to an array, we must first shift all
    #       elements after that index "down" in the array.
    #
    # For i from the size to the given idx, do:
    #     Set the element in the array at i to the element at i - 1.
    #
    # Set the element in the array at the given idx to the given value.
    # Increment the size.
    pass


def remove(lst, idx):
    # NOTE: Just as adding to an array requires shifting elements "down",
    #       removing from an array requires shifting elements "up".
    #
    # For i from the given idx to the size, do:
    #     Set the element in the array at i to the element at i + 1.
    #
    # Decrement the size.
    pass
