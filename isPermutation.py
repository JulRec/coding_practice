# Given a certain array, find out if it's a permutation
# of numbers from 1 to a given integer.

def isPermutation(n, inputArray):
    inputArray.sort()
    for i in range(1,n+1):
        if inputArray[i-1] != i:
            return False

    return True
