def distinct_powers(n):
    seen = set(a ** b for a in range(2, n + 1) for b in range(2, n + 1))
    return str(len(seen))


print(distinct_powers(100))
