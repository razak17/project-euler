from timeit import timeit


def is_pal(x):
    x = str(x)
    t = x[::-1]
    return x == t


def largest_pal_product(n):
    max = 0
    start = n // 10

    for i in range(n, start, -1):
        for j in range(n, start, -1):
            product = i * j
            if is_pal(product) and product > max:
                max = product
    return max


def compute():
	ans = max(i * j
           for i in range(100, 1000)
           for j in range(100, 1000)
           if str(i * j) == str(i * j)[:: -1])
	return str(ans)



print(compute())
print(largest_pal_product(999))

