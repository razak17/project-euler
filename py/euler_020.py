import math
cache = {}


def factorial(n):
    if n in cache:
        return cache[n]
    result = 0
    if n <= 1:
        return 1
    else:
        return factorial_digit_sum(n - 1) * n
    cache[n] = result
    return result


def factorial_digit_sum(x):
    n = math.factorial(x)
    ans = sum(int(i) for i in str(n))
    return str(ans)


print(factorial_digit_sum(100))
