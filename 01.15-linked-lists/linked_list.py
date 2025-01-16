class List:
    """ An ordered collection of elements """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The number of elements in this list:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, value, next):
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next


def get(lst, idx):
    # NOTE: This is the general pattern for "traversing" a linked list: to
    #       access a node in the list, we must start at the head and repeatedly
    #       access each node's next attribute.
    #
    # Start with a current node being the given lst's head.
    # For i from 0 to the given idx:
    #     Set the current node to the current node's next.
    # Return the current node's value.
    pass


def set(lst, idx, value):
    # Start with a current node being the given lst's head.
    # For i from 0 to the given idx:
    #     Set the current node to the current node's next.
    # Set the current node's value to the given value.
    pass


def add(lst, idx, value):
    # Create a new node containing the given value.
    # If the given idx is 0, then:
    #     NOTE: Adding a node to the beginning of a linked list is special,
    #           because it's the only scenario in which there is no previous
    #           node in the list, and we need to change the head instead.
    #
    #     Set the new node's next to the given lst's head.
    #     Set the given lst's head to the new node.
    # Else, do:
    #     NOTE: In general, adding a node to a linked list requires first
    #           finding the previous node in the list, since the previous node
    #           will need a link to the new node.
    #
    #     Start with a current node being the head of the given lst.
    #     For i from 0 to the given idx - 1, do:
    #         Set the current node to the current node's next.
    #     Set the new node's next to the current node's next.
    #     Set the current node's next to the new node.
    # Increment the given lst's size.
    pass


def remove(lst, idx):
    pass
