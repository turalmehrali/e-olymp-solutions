

n = int(input())
ededler = []


for i in range(n):

    m = int(input())

    if abs(m) <= 100:
        ededler.insert(0, m)


print(*ededler, sep=" ")


