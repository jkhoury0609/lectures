import sys


def fibonacci(n):
    """
    Compute Fibonacci numbers.

    :param n: A non-negative integer
    :return: The n'th Fibonacci number
    """

    # NOTE: This function has complexity O(n): the number of operations we
    #       must perform grows linearly with the size of the problem.

    current = previous = None

    for i in range(n + 1):
        if i == 0:
            current = 0
        elif i == 1:
            previous = current
            current = 1
        else:
            temp = previous
            previous = current
            current = current + temp

    return current


if __name__ == "__main__":
    print(fibonacci(int(sys.argv[1])))
