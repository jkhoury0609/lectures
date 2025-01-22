class Stack:
    """ A LIFO collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this stack:
        self.size = 0


def push(stack, value):
    # NOTE: A stack is a special case of a list, a list that can only be
    #       accessed at one terminus. Operating on the end of an array list
    #       is O(1), whereas operating on the beginning is O(n), thus, the end
    #       of the array list ought to be the top-of-stack.
    #
    # If the size is equal to the capacity, then:
    #     Set the capacity to capacity * 2.
    #     Create a new array of that capacity.
    #     (copy the elements from the old array into the new array)
    #     Set the array to the new array.
    #
    # Set the element at the stack's size in the array to the given value.
    # Increment the size.
    pass


def pop(stack):
    # NOTE: Essentially, operating on an array stack is the same as operating
    #       on an array list if the given index was always known to be size or
    #       size - 1, so we don't need any logic for shifting elements.
    #
    # Set a temp variable to the element at size - 1 in the array.
    # Decrement the size.
    # Return the temp variable.
    pass


def peek(stack):
    # Return the element at size - 1 in the array.
    pass
