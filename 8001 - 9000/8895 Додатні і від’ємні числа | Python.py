
ededler = [int(i) for i in input().split()]
b = False

if ededler[0] > 0:
	for i in ededler[1:]:
		if i < 0:
			b = True
			break

elif ededler[0] < 0:
	for i in ededler[1:]:
		if i > 0:
			b = True
			break

if b:
	print("YES")

if not b:
	print("NO")

