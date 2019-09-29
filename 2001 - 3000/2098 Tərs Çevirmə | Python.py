
n = input()
ededler = [int(i) for i in input().split()]
ters = []

for i in ededler:
    ters.insert(0, i)

print(*ters, end=" ")

