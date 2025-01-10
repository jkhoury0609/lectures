import sys


def fibonacci(n):
    """
    Compute Fibonacci numbers.

    :param n: A non-negative integer
    :return: The n'th Fibonacci number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(int(sys.argv[1])))
