def max_element(lst):
    """
    Recursion is the definition of a value in terms of itself, and recursive
     functions are those that call themselves. A function ought to take as
     arguments an instance of a problem, and produce as return value a
     solution to that problem. Thus, a recursive function must identify a
     smaller version of the *same* problem.

    :param lst: A list of comparable elements
    :return: The largest element in lst, or None if lst is empty
    """

    print("lst: %r" % lst)

    # Here, the smallest possible problems are the lists of zero and one
    #  elements. They have different solutions, so they require different
    #  cases:
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]

    # Here, a smaller problem is a shorter list. To find a smaller version of
    #  the same problem, we must remove at least one element from the list:
    else:
        first = lst[0]
        rest = lst[1:]
        temp = max_element(rest)
        print("first: %r, rest: %r, temp: %r" % (first, rest, temp))
        return max(first, temp)

print(max_element([2, -1, 9, 8, 5, -3, 0, 8]))
