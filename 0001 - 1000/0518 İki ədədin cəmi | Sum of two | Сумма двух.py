
n = int(input())
netice = []

for i in range(n):
    ededler = [int(j) for j in input().split()]
    netice.append(sum(ededler))

for i in netice:
    print(i)

