def spiral_diagonal_sum(n):
    """Sum of the diagonals of an n by n matrix
        nb: n must be ODD

    Args:
        n (int): the  number matrix

    Returns:
        int: sum of the diagonals of the n by n matrix
    """
    ans = 1
    ans += sum(4 * i * i - 6 * (i - 1) for i in range(3, n + 1, 2))
    return str(ans)

print(spiral_diagonal_sum(1001))