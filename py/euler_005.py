import fractions


def smallest_multiple(n):
    """The smallest number n that is divisible by every number in a
        set {k1, k2, ..., k_m} is also known as the
        lowest common multiple (LCM) of the set of numbers.

        The LCM of two natural numbers x and y is given by
        LCM(x, y) = x * y / GCD(x, y).

    Arguments:
        n {int} -- the range of numbers.

    Returns:
        int -- smallest positive number that can be divided by
                each of the numbers from 1 to n without
                any remainder.
    """
    res = 1
    for i in range(1, n + 1):
        res *= i // fractions.gcd(i, res)
    return str(res)


print(smallest_multiple(20))
