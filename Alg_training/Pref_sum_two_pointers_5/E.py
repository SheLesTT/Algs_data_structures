n, k = map(int, input().split())
trees = list(map(int, input().split()))


from collections import Counter

color_trees = Counter()
best_length = n+1
coords = ()
left = 0

for right in range(n):
    color_trees[trees[right]] += 1
    if len(color_trees) == k:
        while color_trees[trees[left]] > 1:
            color_trees[trees[left]] -= 1
            left += 1

        if right - left + 1 < best_length:
            best_length = right - left + 1
            coords = (left+1, right+1)

print(*coords)

