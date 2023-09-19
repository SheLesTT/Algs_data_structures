given = int(input())
required = int(input())
# if given == required:
#     print(0)
c1 = int(input())
c2 = int(input())

demand= required - given

ratio = c2/c1
hubs = 0
doublers = 0
if ratio > 4:
    doublers += demand
else:
    hubs += demand//4
    to_by = demand%4
    if to_by > ratio:
        hubs+=1
    else:
        doublers += to_by

if demand < 0:
    print(0)
else:
    print(c1*doublers + c2*hubs)


