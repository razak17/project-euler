# We apply straightforward algorithms to sort the names, sum the letter values, and multiply by the position.


def compute():
	ans = sum((i + 1) * (ord(c) - ord('A') + 1)
           for (i, name) in enumerate(sorted(data))
           for c in name)
	return str(ans)


with open("p022_names.txt") as f:
    d = f.read().split(',')
    data = [name[1:-1] for name in d]
    data.sort()

print(compute())



