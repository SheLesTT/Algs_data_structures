n = int(input())
classes = list(map(int, input().split()))
t = int(input())


best_price  = [1000]*(1000+1)
for _ in range(t):
    power, prise = map(int, input().split())
    # print(prise)
    if best_price[power]> prise:
        # print(power)
        for p in reversed(range(0, power+1)):
            # print(p, best_price[p])
            if best_price[p] > prise:
                best_price[p] = prise
            else:
                break
total = 0
# print(best_price)
for room in classes:
    # print(room)
    # print(best_price[room])
    total += best_price[room]

print(total)