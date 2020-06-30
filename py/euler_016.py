def power_digit_sum(power):
    n = 2 ** power
    result = sum(int(i) for i in str(n))
    return result


print(power_digit_sum(1000))
