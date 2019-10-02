
n = int(input())
b = False

for i in range(1, n):
	kv = i ** 2
	if kv == n:
		b = True
		m = i
		break
	if kv > n:
		break


if b:
	print(m)

if not b:
	print("No")

