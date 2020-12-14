
n = input()

ededler = [int(i) for i in input().split()]

netice = sorted(set(ededler))

print(*netice, sep=" ")

