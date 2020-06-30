def compute(limit):
	divisorsum = [0] * limit
	for i in range(1, limit):
		for j in range(i * 2, limit, i):
			divisorsum[j] += i
	abundantnums = [i for (i, x) in enumerate(divisorsum) if x > i]

	expressible = [False] * limit
	for i in abundantnums:
		for j in abundantnums:
			if i + j < limit:
				expressible[i + j] = True
			else:
				break

	ans = sum(i for (i, x) in enumerate(expressible) if not x)
	return str(ans)


print(compute(28124))
