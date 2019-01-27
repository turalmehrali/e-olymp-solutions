say = input()

ededler = [int(i) for i in input().split()]
boyuk = ededler[0]

for i in ededler:
    if i > boyuk:
        boyuk = i

print(boyuk)
