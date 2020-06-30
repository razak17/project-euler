PERIMETER = 1000

for a in range(1, PERIMETER - 1):
    for b in range(a + 1, PERIMETER + 1):
        c = PERIMETER - a - b

        if a ** 2 + b ** 2 == c ** 2:
            print(a, b, c)
            print(str(a * b * c))
