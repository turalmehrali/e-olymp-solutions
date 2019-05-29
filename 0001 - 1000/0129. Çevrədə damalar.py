
import math

radius = float(input())
dama = 0

for x in range(1, int(radius)):
    dama = int(dama) + math.sqrt(radius ** 2 - x ** 2)

dama = int(dama) * 4
print(dama)
