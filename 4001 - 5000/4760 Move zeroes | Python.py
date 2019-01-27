n = input()
nonzero = []
zeroes = []
ededler = [int(j) for j in input().split()]
for i in ededler:
    if(i != 0):
        nonzero.append(i)
    if(i == 0):
        zeroes.append(i)
print(*(nonzero + zeroes), end="")
