
amount, n = map(int, input().split())
coins = list(map(int, input().split()))



max_usage = 2
dp = [[-1 for _ in range(amount + 1)] for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(amount + 1):
        dp[i][j] = dp[i - 1][j]
        for k in range(1, min(max_usage + 1, j // coins[i - 1] + 1)):
            if dp[i - 1][j - k * coins[i - 1]] != -1 and (dp[i][j] == -1 or dp[i][j] > dp[i - 1][j - k * coins[i - 1]] + k):
                dp[i][j] = dp[i - 1][j - k * coins[i - 1]] + k



stolen_coins = []
i, j = n, amount
while i > 0 and j > 0:
    for k in range(1, max_usage + 1):
        if j >= k * coins[i - 1] and dp[i][j] == dp[i - 1][j - k * coins[i - 1]] + k:
            for _ in range(k):
                stolen_coins.append(coins[i - 1])
            j -= k * coins[i - 1]
    i -= 1

if dp[-1][-1] == -1:
    print(-1)
else:
    print(len(stolen_coins))
    print(*stolen_coins)
