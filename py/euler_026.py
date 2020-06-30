import itertools

def longest_recurring_cycle(n):
    ans = max(range(1, n), key=reciprocal_cycles)
    return str(ans)


def reciprocal_cycles(n):
    seen = {}
    x = 1
    for i in itertools.count():
        if x in seen:
            return i - seen[x]
        else:
            seen[x] = i
            x = x * 10 % n


print(reciprocal_cycles(10))
print(longest_recurring_cycle(1000))
print(10 % 10)
