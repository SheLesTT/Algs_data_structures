n, k = map(int, input().split())
req = n-k
fence = list(map(int, input().split()))

fence = sorted(fence, reverse=True)
sums = [0]
for i in range(n-1):
    sums.append(fence[i]-fence[i+1])



left = 1
right = req

dif = sum(sums[left:right])
diffs = [dif]

while right< len(sums):
    dif -= sums[left]
    left += 1
    right += 1

    dif += sums[right-1]
    diffs.append(dif)


print(min(diffs))

