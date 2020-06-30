import datetime

def counting_sundays(a, b):
    ans = sum(1
        for y in range(a, b + 1)
        for m in range(1, 13)
        if datetime.date(y, m, 1).weekday() == 6
    )
    return str(ans)

print(counting_sundays(1901, 2000))
