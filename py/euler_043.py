import itertools
from itertools import permutations


primes = [2, 3, 5, 7, 11, 13, 17]
s = 0
for i in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    sub = True
    for k in range(1, len(i)-2):
        n = int(''.join([str(x) for x in i[k:k+3]]))
        if n % primes[k-1] != 0:
            sub = False
            break
    if sub:
        s += int(''.join([str(x) for x in i]))

print(s)


# def compute():
#     ans = sum(int("".join(map(str, num)))
#               for num in itertools.permutations(list(range(10)))
#               if is_divisible_substring(num))
#     return str(ans)


# TESTS = [2, 3, 5, 7, 11, 13, 17]


# def is_divisible_substring(num):
#     return all((num[i + 1] * 100 + num[i + 2] * 10 + num[i + 3]) % p == 0
#                for (i, p) in enumerate(TESTS))


# print(compute())
