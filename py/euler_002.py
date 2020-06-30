# Question 2: Even Fibonacci sum

def fib_progression(prev, current, limit):
    total = 0
    if limit <= 0:
        return -1
    else:
        while True:
            if current >= limit:
                break
            if current % 2 == 0:
                total += current
            prev, current = current, prev + current
    return total


def compute():
    ans = 0
    curr = 1
    next = 2
    while curr <= 4000000:
        if curr % 2 == 0:
            ans += curr
        curr, next = next, curr + next
    return str(ans)


# print(fib_progression(1, 2, 4000000))
print(compute())
