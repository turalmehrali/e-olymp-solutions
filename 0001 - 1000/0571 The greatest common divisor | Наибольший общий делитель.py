
from math import gcd

n = input()
ededler = [int(i) for i in input().split()]

ebob = ededler[0]

if len(ededler) == 2:
    ebob = gcd(ededler[0], ededler[1])

elif len(ededler) > 2:

    for i in ededler[2:]:
        ebob = gcd(ebob, i)

print(ebob)


