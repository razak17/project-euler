def largest_1_to_9_pandigital():
    ans = ""
    for n in range(2, 10):
        for i in range(10 ** (9 // n)):
            s = "".join(str(i * j) for j in range(1, n + 1))
            if "".join(sorted(s)) == "123456789":
                ans = max(s, ans)
    return ans

print(largest_1_to_9_pandigital())
