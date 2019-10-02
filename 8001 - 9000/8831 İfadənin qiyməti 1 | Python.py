
ededler = [float(i) for i in input().split()]
x = ededler[0]
y = ededler[1]

z = 2 * x ** 2 - 4 * x * y + 3 * y ** 2 + (x + y) / 7

print("{0:.3f}".format(z))

