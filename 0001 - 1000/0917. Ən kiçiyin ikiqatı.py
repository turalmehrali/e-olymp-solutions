h = input()
ededler = [float(i) for i in input().split()]
kicik = ededler[0]

for j in ededler:
    if j < kicik:
        kicik = j

print('{0:.2f}'.format(kicik * 2))
