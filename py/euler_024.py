import itertools


# We initialize a list as the lowest permutation of the given digits, which is the sequence
# (0,1,2,3,4,5,6,7,8,9). Then we call a Python library function that generates a stream of
# all permutations of the values, seek to the 999 999th element (0-based indexing), and stringify it.
def lex_permutation(aList, n):
    """Find the lexographic pern=mutaition for a list of numbers

    Args:
        aList (list): list of numbers
        n (number): nth lex postion of aList

    Returns:
        [number]: nth lex permutaion of nums in aList
    """
    temp = itertools.islice(itertools.permutations(aList), n - 1, None)
    return "".join(str(x) for x in next(temp))


print(lex_permutation(list(range(10)), 1000000))
