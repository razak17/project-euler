import itertools

# index of the first term in the Fibonacci sequence to contain n digits


def fib_with_n_digits(n):
    """First number in the fibonacci sequence with n digits

    Args:
        n (number): number of digits of fibonnaci number
    """
    # n = 1000
    prev = 1
    cur = 0
    for i in itertools.count():
        # At this point, prev = fibonacci(i - 1) and cur = fibonacci(i)
        if len(str(cur)) > n:
            raise RuntimeError("Not found")
        elif len(str(cur)) == n:
            return str(i)

        # Advance the Fibonacci sequence by one step
        prev, cur = cur, prev + cur


print(fib_with_n_digits(1000))
