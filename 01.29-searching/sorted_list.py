class SortedList:
    """ A sorted collection of elements """

    def __init__(self):
        # NOTE: In order to take advantage of the knowledge that the elements
        #       are sorted, we have to be able to randomly access the element
        #       in the middle, which means this must be an array list.

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
    # NOTE: Since the list is known to be sorted, comparing the middle element
    #       to the given value gives us information about more than just that
    #       one element. If, for example, the middle element is too small, then
    #       all prior elements are also too small.
    #
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
    # NOTE: To reach this point, the low index must be greater than the high
    #       index, meaning that the sublist yet to be searched is empty. That
    #       is, there are no elements left in the list that might be equal to
    #       the given value -- the given value does not exist.
    #
    # Return (the given value is not in the given list).
    pass


def create(array, size):
    pass
