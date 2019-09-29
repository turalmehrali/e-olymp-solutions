
n = input()
ededler = [int(i) for i in input().split()]
netice = []
kicik = min(ededler) // 2

for i in ededler:
    i -= kicik
    netice.append(str(i))

print(" ".join(netice))

