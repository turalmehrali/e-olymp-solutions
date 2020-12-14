
ededler = [int(i) for i in input().split()]

say = ededler[0]

ededler.remove(say)

maxpoint = max(ededler)
minpoint = min(ededler)

counter = 0

for i in ededler:
    if i == maxpoint:
        ededler[counter] = minpoint

    counter += 1

print(*ededler, sep=" ")

