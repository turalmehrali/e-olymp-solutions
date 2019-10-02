
ededler = [float(i) for i in input().split()]
x = ededler[0]
y = ededler[1]

z = 2 * x * y / ((x ** 2 + y ** 2) ** 0.5) - ((x + y - 1) ** 2) / (x * y)

print("{0:.3f}".format(z))

