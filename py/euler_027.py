from helpers import list_primality, is_prime as prime
import itertools


def quadratic_primes():
    ans = max(((a, b)
               for a in range(-999, 1000)
               for b in range(2, 1000)),
              key=consecutive_prime_count)
    return str(ans[0] * ans[1])


def consecutive_prime_count(n):
    a, b = n
    for i in itertools.count():
        n = i * i + i * a + b
        if not is_prime(n):
            return i


prime_cache = list_primality(1000)


def is_prime(n):
    if n < 0:
        return False
    elif n < len(prime_cache):
        return prime_cache[n]
    else:
        return prime(n)


print(is_prime(21))
print(consecutive_prime_count([2, 21]))
print(quadratic_primes())
