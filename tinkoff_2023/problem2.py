string  = input()

d = {"s":0, "h":0,"e":0,"r":0,"i":0,"f":0}

for letter in string:
    if letter in d.keys():
        d[letter] += 1

d["f"] = d["f"]//2
print(min(d.values()))