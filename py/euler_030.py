

def fifth_digit_power_sum():
    ans = sum(i for i in range(2, 1000000) if i == digit_power(i))
    return str(ans)


def digit_power(n):
    return sum(int(c) ** 5 for c in str(n))


print(fifth_digit_power_sum())
