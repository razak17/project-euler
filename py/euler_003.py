import helpers


def highest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
        i += 1
    return n


def compute(n):
	while True:
		p = smallest_prime_factor(n)
		if p < n:
			n //= p
		else:
			return str(n)

def smallest_prime_factor(n):
    assert n >= 2
    for i in range(2, helpers.sqrt(n) + 1):
        if n % i == 0:
            return i
    return n


print(highest_prime_factor(600851475143))
print(compute(600851475143))
print(smallest_prime_factor(13))
