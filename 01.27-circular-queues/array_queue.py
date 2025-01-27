class Queue:
    """ A FIFO collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity

        # NOTE: With a list, in order to support fast random access, elements'
        #       indices must range between 0 and size - 1. With a queue, we
        #       don't actually care about the indices themselves, so we'll have
        #       elements between front and back, with the hope of avoiding any
        #       need for shifting...

        # The index of the front of the queue:
        self.front = -1
        # The index of the back of the queue:
        self.back = -1


def enqueue(queue, value):
    # NOTE: ...in order to avoid shifting, elements need not start at index 0.
    #       However, in order to avoid wasting space before the front, the back
    #       must be allowed to "wrap around". Three possibilities exist:
    #         * If front < 0 and back < 0, then there are no elements.
    #         * If front <= back, then the elements are [front : back + 1].
    #         * Else, the elements are [front : capacity] + [0, back + 1].
    #       ...when increasing capacity, the elements will need to be shifted
    #       in order to unwrap them, but that's okay because copying them was
    #       aleady going to require iterating over the whole array anyways.
    #
    # If (the queue has capacity elements), then:
    #     Set the capacity to capacity * 2.
    #     Create a new array of that capacity.
    #     (copy the elements from the old array into the new array and "unwrap"
    #      them such that front is 0)
    #     Set the array to the new array.
    #
    # If (the queue has no elements), then:
    #     Set the front and back to 0.
    # Else, do:
    #     Increment back and mod it by capacity.
    #
    # Set the element at back in the array to the given value.
    pass


def dequeue(queue):
    # If (the queue has one element), then:
    #     Set the front and back to -1.
    # Else, do:
    #     Increment front and mod it by capacity.
    pass


def peek(queue):
    # Return the element at front in the array.
    pass
