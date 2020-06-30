import helpers
RANGE = 2000000


def compute():
    ans = sum(helpers.list_primes(1999999))
    return str(ans)


total = 0

for i in range(2, RANGE):
    if (helpers.is_prime(i) == True):
        total += i
print(total)
print(compute())
