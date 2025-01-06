def max_element(lst):
    """
    :param lst: A list of comparable elements
    :return: The largest element, or None if empty.
    """

    # Recursion is the definition of a value in terms of itself, and recursive
    #  functions therefore must call themselves. A function ought to take as
    #  arguments an instance of a problem and produce as output a solution to
    #  that problem. Thus, a recursive function must identify a smaller version
    #  of the *same* problem.

    # Here, the smallest possible problems are the lists of zero and one
    #  elements, which have two different solutions, so they must be two
    #  different cases:
    if len(lst) == 0:
        print("lst: %r" % lst)
        return None
    elif len(lst) == 1:
        print("lst: %r" % lst)
        return lst[0]

    # Here, a shorter list is a smaller version of the same problem -- we still
    #  have the same type of argument and we still expect the same type of
    #  return value, we just have one fewer element in list:
    else:
        print("lst: %r" % lst)
        first = lst[0]
        rest = max_element(lst[1:])
        print("lst: %r, first: %r, rest: %r" % (lst, first, rest))
        return max(first, rest)

print(max_element([2, -1, 9, 8, 5, -3, 0, 8]))
