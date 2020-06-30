def amicable_nums(n):
    # Compute sum of proper divisors for each number
    aList = []
    divisorsum = [0] * n
    for i in range(1, len(divisorsum)):
        for j in range(i * 2, len(divisorsum), i):
            divisorsum[j] += i

    # Find all amicable pairs within range
    ans = 0
    for i in range(1, len(divisorsum)):
        j = divisorsum[i]
        if j != i and j < len(divisorsum) and divisorsum[j] == i:
            ans += i
            aList.append(i)
    print(aList)
    return str(ans)


print(amicable_nums(10000))
