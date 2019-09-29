
n = input()
ededler = [int(i) for i in input().split()]
netice = []
boyuk = ededler[0]

for i in ededler:
	if i > boyuk:
	    boyuk = i
	    indeks = ededler.index(i) + 1


print(boyuk, indeks)

