say = input()
ededler = [int(i) for i in input().split()]

boyuk = ededler[0]
kicik = ededler[0]

for j in ededler:
    if j > boyuk:
        boyuk = j

    if j < kicik:
        kicik = j

print(boyuk - kicik)
