
ededler = []
cem = 0
a = True

while a:
	n = int(input())
	if n == 0:
		a = False
	else:
		ededler.append(n)

for i in ededler:
	if i % 2 == 0:
		cem += i

print(cem)

