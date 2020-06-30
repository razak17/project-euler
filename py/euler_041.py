import helpers

def compute():
	# Note: The only 1-digit pandigital number is 1, which is not prime. Thus we require n >= 2.
	for n in reversed(range(2, 10)):
		arr = list(reversed(range(1, n + 1)))
		while True:
			if arr[-1] not in NONPRIME_LAST_DIGITS:
				n = int("".join(str(x) for x in arr))
				if helpers.is_prime(n):
					return str(n)
			if not prev_permutation(arr):
				break
	raise AssertionError()

NONPRIME_LAST_DIGITS = {0, 2, 4, 5, 6, 8}


def prev_permutation(aList):
	i = len(aList) - 1
	while i > 0 and aList[i - 1] <= aList[i]:
		i -= 1
	if i <= 0:
		return False
	j = len(aList) - 1
	while aList[j] >= aList[i - 1]:
		j -= 1
	aList[i - 1], aList[j] = aList[j], aList[i - 1]
	aList[i : ] = aList[len(aList) - 1 : i - 1 : -1]
	return True


print(compute())
