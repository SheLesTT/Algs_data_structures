from math import factorial
import numpy as np
print(factorial(17))

l =[]
n=17
for k in range(18):
    val = ((factorial(n)/factorial(n-k))*7*10*factorial(32-k)*(k+1))/factorial(34)
    l.append(val)
print(sum(l))
# for k in range(18):
#     val = ((factorial(n)/((n-k)!))*7*10*(32-k)!*(k+1))/34!