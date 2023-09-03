n = int(input())

given = list(map(int, input().split()))
winning = list(map(int, input().split()))

start, end = -1, -1
for i in range(n):
    if given[i] != winning[i]:
        if start == -1:
            start = i
            end = i
        else:
            end = i
given[start:end+1] = sorted(given[start:end+1])
if given == winning:
    print("YES")
else:
    print("NO")