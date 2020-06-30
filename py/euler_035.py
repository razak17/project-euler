import helpers

def circular_primes(n):
    isprime = helpers.list_primality(n - 1)
    def is_circular_prime(n):
        s = str(n)
        return all(isprime[int(s[i:] + s[:i])] for i in range(len(s)))

    ans = sum(1 for i in range(len(isprime)) if is_circular_prime(i))
    return str(ans)

print(circular_primes(1000000))