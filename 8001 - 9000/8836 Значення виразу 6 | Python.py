
ededler = [float(i) for i in input().split()]
x = ededler[0]
y = ededler[1]

z = (x - y) ** 2 / ((x ** 2 + y ** 2 - 1) ** 0.5) + (x ** 2 + y ** 2 - 1) ** 0.5 / (2 * x * y)

print("{0:.3f}".format(z))

