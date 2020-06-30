import helpers


def compute():
    # arbitrary upper limit
    PRIME_LIMIT = 100000
    # list of all primes below PRIME_LIMIT
    primes = helpers.list_primes(PRIME_LIMIT)

    def find_set_sum(prefix, targetsize, sumlimit):
        """Tries to find a suitable set and return its sum.
        A suitable set is one that contains only primes, has the
        size of targetsize, a sum less than or equal to
        sumlimit and each pair concats to a prime.
        NB: The function blindly assumes that each pair of primes
            in 'prefix' concatenates to a prime.

        Arguments:
            prefix {list} -- array of ascending indices in to the primes array
            targetsize {int} -- size of the set of primes
            sumlimit {int} -- sum limit of the set

        Returns:
            int -- sum of suitable set of primes
        """
        if len(prefix) == targetsize:
            return sum(primes[i] for i in prefix)
        else:
            istart = 0 if (len(prefix) == 0) else (prefix[-1] + 1)
            for i in range(istart, len(primes)):
                if primes[i] > sumlimit:
                    break
                if all((is_concat_prime(i, j) and is_concat_prime(j, i)) for j in prefix):
                    prefix.append(i)
                    result = find_set_sum(prefix, targetsize, sumlimit - primes[i])
                    prefix.pop()
                    if result is not None:
                        return result
            return None

    @helpers.memoize
    def is_concat_prime(x, y):
        return is_prime(int(str(primes[x]) + str(primes[y])))

    def is_prime(x):
        if x < 0:
            raise ValueError()
        elif x in (0, 1):
            return False
        else:
            end = helpers.sqrt(x)
            for p in primes:
                if p > end:
                    break
                if x % p == 0:
                    return False
            for i in range(primes[-1] + 2, end + 1, 2):
                if x % i == 0:
                    return False
            return True

    sumlimit = PRIME_LIMIT
    while True:
        setsum = find_set_sum([], 5, sumlimit - 1)
        if setsum is None:  # No smaller sum found
            return str(sumlimit)
        sumlimit = setsum


if __name__ == "__main__":
    print(compute())
