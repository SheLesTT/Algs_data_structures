side_walks , digs, repairs = map(int, input().split())
d= {}
diffs = []
for dig in range(digs):
    day, walk = map(int, input().split())
    if walk not in d:
        # print(walk)
        d[walk] = [day]
    else:

        diffs.append(day - d[walk][-1])
        d[walk].append(day)

sadness = 0

for walk in d:
    sadness+= d[walk][-1] - d[walk][0]
repairs -= len(d)
if repairs< 0:
    print(-1)
elif repairs == 0:
    print(sadness)
else:
    diffs = sorted(diffs)
    while repairs and diffs:

        elm = diffs.pop()
        sadness -= elm
        repairs -= 1
    print(sadness)


