"""
Task
In schools in the country known as Codelandia, a special five-point grading
scale is used. Each grade is a English letter from 'A' to 'E' with a value from
 5 to 1 respectively. A student is considered to have passed the class if the
 average value of their grades is greater than or equal to the passing mark.
 Given the passing mark and a student's grades, find out if they have
 successfully passed the class or not.
"""

import doctest

def passingMark(passMark, grades):
    """
    Calculate if a string of grades is greater or equal to the passing mark

    :param passMark: Float, between 1.0 and 5.0
    :param grades: String, any combination of A, B, C, D, E
    :return: bool, greater or equal passing mark = True, lesser = False

    >>> passingMark(3.5, "ABC")
    True

    >>> passingMark(4, "BBCD")
    False

    >>> passingMark(1, "DEEEEEEEE")
    True

    """
    result = 0
    count = 0
    for i in grades:
        if i == "A":
            result += 5
        elif i == "B":
            result += 4
        elif i == "C":
            result += 3
        elif i == "D":
            result += 2
        else:
            result += 1
        count += 1

    if result/count >= passMark:
        return True
    else:
        return False

# --- Tests --------------------------------------------------------------------
if __name__ == "__main__":
    doctest.testmod()
