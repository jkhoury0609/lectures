class Queue:
    """ A FIFO collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity

        # NOTE: With a list, elements must be shifted on add/remove in order to
        #       ensure that indices range between 0 and size - 1. With a queue,
        #       don't actually care about the indices, so we'll allow them to
        #       range between some arbitrary front and some arbitrary back:

        # The index of the front of the queue:
        self.front = -1
        # The index of the back of the queue:
        self.back = -1


def enqueue(queue, value):
    # NOTE: Since the front need not be index 0, it is possible that there is
    #       extra space in the array before the front -- the back needs to be
    #       able to "wrap around" to fill the space. Three possibilities exist:
    #         * If front < 0 and back < 0, then the elements are [].
    #         * If front <= back, then the elements are [front : back + 1].
    #         * Else, the elements are [front : capacity] + [0 : back + 1].
    #       ...when increasing capacity, the elements will need to be shifted
    #       in order to "unwrap" them, but that's okay because copying them was
    #       aleady going to require iterating over the whole array anyways.
    #
    # If (the queue has capacity elements), then:
    #     Set the capacity to capacity * 2.
    #     Create a new array of that capacity.
    #     (copy the elements from the old array into the new array and "unwrap"
    #      them such that the front is once again at index 0)
    #     Set the array to the new array.
    #
    # If (the queue has no elements), then:
    #     Set the front and the back to 0.
    # Else, do:
    #     Increment the back and mod it by the capacity.
    #
    # Set the element at back in the array to the given value.
    pass


def dequeue(queue):
    # If (the queue has one element), then:
    #     Set the front and the back to -1.
    # Else, do:
    #     Increment the front and mod it by the capacity.
    pass


def peek(queue):
    # Return the element at front in the array.
    pass
