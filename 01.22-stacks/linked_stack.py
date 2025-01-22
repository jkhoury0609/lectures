class Stack:
    """ A LIFO collection of elements """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The number of elements in this stack:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, value, next):
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next


def push(stack, value):
    # NOTE: A stack is a list that can only be operated on at one terminus.
    #       Adding and removing at the beginning of a linked list is O(1), but
    #       adding and removing at the end of a linked list is O(n). Thus, the
    #       beginning of the linked list ought to be the top-of-stack.
    #
    # Create a new node containing the given value.
    # Set the new node's next to the given stack's head.
    # Set the given stack's head to the new node.
    # Increment the given stack's size.
    pass


def pop(stack):
    # NOTE: Essentially, operating on a linked stack is the same as operating
    #       on a linked list if the given index was always known to be 0.
    #
    # Set a temp variable to the given stack's head's value.
    # Set the given stack's head to the given stack's head's next.
    # Decrement the given stack's size.
    # Return the temp variable.
    pass


def peek(stack):
    # Return the given stack's head's value.
    pass
