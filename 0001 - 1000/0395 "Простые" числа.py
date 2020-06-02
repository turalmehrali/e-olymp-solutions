
n = input()
ededler = [int(i) for i in input().split()]
netice = []

for i in ededler:
    say = 0
    for j in ededler:
        if i % j == 0:
            say += 1

    if say == 1:
        netice.append(i)


print(*netice, sep=" ")

