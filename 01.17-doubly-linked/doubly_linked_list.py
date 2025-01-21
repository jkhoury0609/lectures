class List:
    """ An ordered collection of elements """

    def __init__(self):
        # The head of the backing doubly linked list:
        self.head = None
        # The tail of the backing doubly linked list:
        self.tail = None;
        # The number of elements in this list:
        self.size = 0


class Node:
    """ A single node in a doubly linked list """

    def __init__(self, value, previous, next):
        # The value contained in this node:
        self.value = value
        # The previous node in the linked list:
        self.previous = previous
        # The next node in the linked list:
        self.next = next


def get(lst, idx):
    # TODO: Check to see if the given idx is in the second half of the list, in
    #       which case we could insted start at the tail and traverse the list
    #       backwards? This seems like a clever idea, but it's not actually any
    #       faster as the list grows arbitrarily large -- it still cannot
    #       support fast "random access".
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
    # If the given lst's size is 0, then:
    #     NOTE: With a doubly linked list, we need a special case for adding to
    #           an empty list, which is the unique scenario in which the new
    #           node is both the head and the tail.
    #
    #     Set the new node's next to None.
    #     Set the new node's previous to None.
    #     Set the given lst's head to the new node.
    #     Set the given lst's tail to the new node.
    # Else if the given idx is 0, then:
    #     NOTE: We do still need a special case for adding to the beginning of
    #           a non-empty list, it's just that in this case the new node is
    #           only the head, but not the tail.
    #
    #     Set the new node's next to the given lst's head.
    #     Set the new node's previous None.
    #     Set the given lst's head's previous to the new node.
    #     Set the given lst's head to the new node.
    # Else if the given idx is the given lst's size, then:
    #     NOTE: Just as a singly linked list must special case adding to the
    #           head, a doubly linked list must also special case adding to
    #           the tail.
    #
    #     Set the new node's next to None.
    #     Set the new node's previous to the given lst's tail.
    #     Set the given lst's tail's next to the new node.
    #     Set the given lst's tail to the new node.
    # Else, do:
    #     Start with a current node being the head of the given lst.
    #     For i from 0 to the given idx - 1, do:
    #         Set the current node to the current node's next.
    #     Set the new node's next to the current node's next.
    #     Set the new node's next's previous to the new node.
    #     Set the current node's next to the new node.
    #     Set the new node's previous to the current node.
    # Increment the given lst's size.
    pass


def remove(lst, idx):
    pass
