def coin_sums():
    n = 200

    ways = [1] + [0] * n
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    for coin in coins:
        for i in range(len(ways) - coin):
            ways[i + coin] += ways[i]
    return str(ways[-1])

print(coin_sums())
