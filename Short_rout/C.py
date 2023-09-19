t= int(input())

tree= {0: 0}
max_level = 0
elem = None
for i in range(t):
    root= int(input())
    level = tree[root] +1
    tree[i+1]= level
    if level > max_level:
        max_level = level
        elem = i+1

print(elem)

