def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

def sum_square_difference(n):
    squares_sum = sum_of_squares(n)
    s = sum(i for i in range(1, n + 1))
    return (s ** 2) - squares_sum

print(sum_of_squares(100))
print(sum_square_difference(100))
