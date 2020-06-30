# Question 1: Modulo sum(3, 5)

# sum = 0
# n = 1000
# for i in range(n):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i


def compute():
	ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
	return str(ans)
print(compute())
