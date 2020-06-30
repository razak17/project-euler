import itertools


def triangular_words():
    ans = sum(1
              for s in data
              if is_triangular_number(sum((ord(c) - ord('A') + 1) for c in s)))
    return str(ans)


def is_triangular_number(n):
    temp = 0
    for i in itertools.count():
        temp += i
        if n == temp:
            return True
        elif n < temp:
            return False


with open("p042_words.txt") as f:
    d = f.read().split(',')
    data = [name[1:-1] for name in d]
    data.sort()

print(triangular_words())
