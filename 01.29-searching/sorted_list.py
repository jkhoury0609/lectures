class SortedList:
    """ A sorted collection of elements """

    def __init__(self):
        # NOTE: In order to take advantage of the fact that the list is known
        #       to be sorted, we have to be able to jump to the middle element,
        #       so this must be an array list rather than a linked list.

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
    #       gives us information about more than just that element. If, for
    #       example, the middle element is too small, then all elements in the
    #       first half of the list must also be too small.
    #
    # Start with the low index being 0 and the high index being size - 1.
    #
    # While the low index is less than or equal to the high index, do:
    #     Set the mid index to (low + high) // 2.
    #     If the element at mid in the array is equal to the given value, then:
    #         Return mid.
    #     Else if the element at mid is less than the given value, then:
    #         Set the low index to mid + 1.
    #     Else, do:
    #         Set the high index to mid - 1.
    #
    # NOTE: To get here, the low index must be greater than the high index;
    #       that is, the sublist of elements to be searched is empty, and
    #       the given value does not exist in the list at all.
    #
    # Return (the given value does not exist).
    pass


def create(array, size):
    pass
