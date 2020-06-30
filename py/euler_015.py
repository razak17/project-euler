from helpers import binomial


def lattice_paths(n):
    return str(binomial(n * 2, n))


print(lattice_paths(20))
