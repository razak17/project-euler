from helpers import memoize
import sys

def longest_collatz_chain_sequence(n):
    sys.setrecursionlimit(3000)
    ans = max(range(1, n), key=collatz_chain_sequence)
    return str(ans)

@memoize
def collatz_chain_sequence(x):
    if x == 1:
        return 1
    if x % 2 == 0:
        y = x // 2
    else:
        y = 3 * x + 1

    return collatz_chain_sequence(y) + 1


print(collatz_chain_sequence(13))
print(longest_collatz_chain_sequence(1000000))
