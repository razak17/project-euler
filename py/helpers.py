import math

def sqrt(n):
    """Determines the integer floor square root of a number.

    Arguments:
        n {int} -- int to determine sqrt of.

    Returns:
        int -- square root of n
    """
    assert n >= 0
    i = 1
    while i * i <= n:
        i *= 2
    j = 0
    while i > 0:
        if (j + i)**2 <= n:
            j += i
        i //= 2
    return j

def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, sqrt(x) + 1, 2):
			if x % i == 0:
				return False
		return True
print(is_prime(5))


def binomial(n, k):
	assert 0 <= k <= n
	return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))



def list_primality(n):
    """Uses Sieve of Eratosthenes to determine
        whether integers up to n are prime or not.
        For 0 <= i <= n, result[i] is True if i is prime
        and False otherwise.

    Arguments:
        n {int} -- count of primes.

    Returns:
        list of bools -- True if a number is prime and False otherwise.
    """
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(sqrt(n) + 1):
        if result[i] == True:
            for j in range(i * i, len(result), i):  # Multiples
                result[j] = False
    return result

print(list_primality(5))


def list_primes(n):
    """Returns all prime numbers less than or equal to n.

    Arguments:
        n {int} -- limit for prime numbers

    Returns:
        list -- list of all prime numbers <= n
                eg. list_primes(29) = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]


# Decorator. The underlying function must take only positional arguments, no keyword arguments.
class memoize:

	def __init__(self, func):
		self.func = func
		self.cache = {}

	def __call__(self, *args):
		if args in self.cache:
			return self.cache[args]
		else:
			val = self.func(*args)
			self.cache[args] = val
			return val


