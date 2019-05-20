
ededler = [float(i) for i in input().split()]
cem = ededler[0] + ededler[1] + ededler[2]

cavab = min(max(ededler[0], ededler[1]), max(ededler[1], ededler[2]), cem)

print('{:0.2f}'.format(cavab))
