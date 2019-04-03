"""
Task
Every positive integer can be uniquely represented as a sum of different positive powers of two.
Given a number n, return a sorted array of different powers of two that sum up to n.
"""

import doctest


def powers_of_two(n):
    """
    Given a number n, return a sorted array of different powers of two that sum up to n
    :param n: Integer, positive
    :return: an array of different powers of two, in ascending order

    >>> powers_of_two(5)
    [1, 4]

    >>> powers_of_two(10)
    [2, 8]

    >>> powers_of_two(127)
    [1, 2, 4, 8, 16, 32, 64]

    """

    n = str(bin(n))[2:]
    # print("DEBUG n =", n)
    result = []
    for i in range(len(n)):
        # print ("DEBUG i+1, n[-(i+1)]", i+1, n[-(i+1)])
        if int(n[-(i + 1)]) == 1:
            result.append(2 ** i)

    return result


# --- Tests --------------------------------------------------------------------
if __name__ == "__main__":
    doctest.testmod()
