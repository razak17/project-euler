from helpers import sqrt
from itertools import count


def divisors(n):
    result = sum(2
                 for i in range(1, sqrt(n) + 1)
                 if n % i == 0
                 )
    if sqrt(n) ** 2 == n:
        result -= 1
    return result


def hd_triangular_number(limit):
    triangle = 0
    for i in count(1):
        # This is the ith triangle number, i.e. num = 1 + 2 + ... + i = i * (i + 1) / 2
        triangle += i
        if divisors(triangle) > limit:
            return str(triangle)


print(hd_triangular_number(500))
