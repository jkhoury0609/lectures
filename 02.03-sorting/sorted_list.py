class SortedList:
    """ A sorted collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this sorted list:
        self.size = 0


def insert(lst, value):
    pass


def remove(lst, idx):
    pass


def find(lst, value):
    # Start with the low index being 0 and the high index being size - 1.
    #
    # While the low index is less than or equal to the high index, do:
    #    Set the mid index to (high + low) // 2.
    #    If the element at mid in the array is equal to the given value, then:
    #        Return mid.
    #    Else if the element at mid is less than the given value, then:
    #        Set the low index to mid + 1.
    #    Else, do:
    #        Set the high index to mid - 1.
    #
    # Return (the given value is not in the given list).
    pass


def create(array, size):
    pass
