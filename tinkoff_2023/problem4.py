sum_to_still, amount = map(int, input().split())
coins = list(map(int, input().split()))

dp = [[]for _ in range(sum_to_still+1)]
dp[0].append({})

for number in range(sum_to_still):
    print(number)
    print(dp)
    if len(dp[number]) != 0:
        for coin in coins:
            if number+coin <= sum_to_still:
                for way in dp[number]:
                    if coin not in way.keys():
                        new_way = way.copy()
                        new_way[coin] = 1
                        dp[number+coin].append(new_way)
                    else:
                        if way[coin] < 2:
                            new_way = way.copy()
                            new_way[coin] +=1
                            dp[number+coin].append(new_way)
            if len(dp[-1]) != 0:
                break
l = []
if len(dp[-1]) != 0:
    for key, val in dp[-1][0].items():
        if val ==1 :
            l.append(key)
        else:
            l.append(key)
            l.append(key)

    for val in l:
        print(val, end=" ")
else:
    print(-1)