import helpers, itertools


def is_truncatable_prime(n):
    # Left truncatable
    i = 10
    while i <= n:
        if not helpers.is_prime(n % i):
            return False
        i *= 10
    # Right truncatable
    while n > 0:
        if not helpers.is_prime(n):
            return False
        n //= 10
    return True


def truncatable_primes_sum():
    ans = sum(itertools.islice(
        filter(is_truncatable_prime, itertools.count(10)), 11))
    return str(ans)


print(is_truncatable_prime(3797))
print(truncatable_primes_sum())
