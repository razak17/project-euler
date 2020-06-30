def is_decimal_binary_palindrome(n):
    s = str(n)
    if s != s[::-1]:
        return False
    t = bin(n)[2:]
    return t == t[::-1]


def sum_double_base_palindrome():
    ans = sum(i for i in range(1, 1000000) if is_decimal_binary_palindrome(i))
    return str(ans)

print(is_decimal_binary_palindrome(585))
print(sum_double_base_palindrome())