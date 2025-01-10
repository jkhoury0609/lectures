import sys


def fibonacci(n):
    """
    Compute Fibonacci numbers.

    :param n: A non-negative integer
    :return: The n'th and (n - 1)'st Fibonacci numbers
    """

    # NOTE: This function had complexity O(1.65^n), but *not* because it was
    #       written recursively. Rather, the recursive case does a lot more
    #       work than it should need to. Suppose we wish to compute f(4):
    #        1. By definition, f(4) = f(3) + f(2).
    #        2. First, we compute f(3) = f(2) + f(1).
    #           ...
    #        3. Then, we compute f(2) again.
    #       ...doing work recursively is not inherently inefficient. The issue
    #       is that this function was doing the *same work multiple times*.

    if n == 0:
        return (0, None)
    elif n == 1:
        return (1, 0)
    else:
        current, previous = fibonacci(n - 1)
        return (current + previous, current)


if __name__ == "__main__":
    print(fibonacci(int(sys.argv[1])))
