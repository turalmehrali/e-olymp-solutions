
ededler = [float(i) for i in input().split()]
x = ededler[0]
y = ededler[1]

z = (x ** 2 - 2 * x * y + 4 * y ** 2) / (x + 5) + (3 * x ** 2 - y ** 2) / (y - 7)

print("{0:.3f}".format(z))

