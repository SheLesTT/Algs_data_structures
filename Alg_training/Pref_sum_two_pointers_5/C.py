n = int(input())
up_sum = [0]
down_sum = [0]
x, prev_y = map(int, input().split())
for _ in range(n-1):
    x, y = map(int, input().split())
    if y - prev_y >0:
        up_sum.append(up_sum[-1] + y - prev_y)
        down_sum.append(down_sum[-1])
    else:
        up_sum.append(up_sum[-1])
        down_sum.append(down_sum[-1] + y - prev_y)
    prev_y = y
m = int(input())
# print(up_sum
tests = []
for _ in range(m):
    x, y = map(int, input().split())
    tests.append((x, y))
for x, y in tests:
    if y > x:
        print(up_sum[y-1] - up_sum[x-1])
    else:
        print(down_sum[y-1] - down_sum[x-1])


