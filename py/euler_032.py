import helpers


def pandigital_products_sum():
    ans = sum(i for i in range(1, 10000) if has_pandigital_product(i))
    return ans


def has_pandigital_product(n):
    for i in range(1, helpers.sqrt(n) + 1):
        if n % i == 0:
            temp = str(n) + str(i) + str(n // i)
            if "".join(sorted(temp)) == "123456789":
                return True
    return False


print(pandigital_products_sum())
