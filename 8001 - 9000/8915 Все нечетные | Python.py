
ededler = []
n = int(input())

for i in range(1, n):
	if i % 2 != 0:
		ededler.append(i)

print(*ededler, end=" ")

