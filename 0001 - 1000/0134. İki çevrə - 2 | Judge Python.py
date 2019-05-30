cavab = 0

o1x, o1y, r1, o2x, o2y, r2 = input().split()
o1x = int(o1x)
o1y = int(o1y)
r1 = int(r1)
o2x = int(o2x)
o2y = int(o2y)
r2 = int(r2)

for x in range(-300, 300):
    for y in range(-300, 300):
        if (o1x - x) * (o1x - x) + (o1y - y) * (o1y - y) <= r1 * r1 or (o2x - x) * (o2x - x) + (o2y - y) * (o2y - y) <= r2 * r2:
            cavab += 1

print(cavab)
