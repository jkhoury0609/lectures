def fibonacci(n):
    """
    Compute the n'th Fibonacci number.

    :param n: A non-negative integer
    :return: The corresponding Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
