
ededler = [float(i) for i in input().split()]
x = ededler[0]
y = ededler[1]

z = (2 * x + y) / (x ** 2 - x * y + 4 * y ** 2) + (2 * x ** 2 - x * y + y ** 2) / (x + 4 * y)

print("{0:.3f}".format(z))

