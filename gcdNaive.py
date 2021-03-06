def gcdNaive(a, b):

    gcd = 1
    for divisor in range(2, min(a, b) + 1):
        if a % divisor == 0 and b % divisor == 0:
            gcd = divisor

    return gcd
