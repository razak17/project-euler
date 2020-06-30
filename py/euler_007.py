import itertools
import helpers


def nth_prime_number(n):
    ans = next(itertools.islice(
        filter(helpers.is_prime, itertools.count(2)), n, None))
    return str(ans)


print(nth_prime_number(10000))