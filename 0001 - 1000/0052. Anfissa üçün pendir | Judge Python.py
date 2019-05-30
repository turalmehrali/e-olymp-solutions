

import math
a, h, z = input().split()
a = int(a)
h = int(h)
z = int(z)

c = z * math.pi / 180
d = math.sin(c) / math.cos(c)

if z == 90:
    cavab = a * h * math.sqrt(2)
elif 2 * h < a * d:
    cavab = (a * a / 2 - (a - h * math.sqrt(2) / d) ** 2 / 2) / math.cos(c)

else:
    cavab = a * a / 2 / math.cos(c)

print("{0:.3f}".format(cavab))
