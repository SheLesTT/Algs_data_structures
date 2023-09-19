n , r= map(int,input().split())
nums = list(map(int, input().split()))

left = right = 0
count = 0
for i in range(n):

    while nums[right] - nums[i]<=r:
        right += 1
        if right > n-1:
            break

    if right > n-1:
        break
    count += n - right
    print(right, count)

print(count)