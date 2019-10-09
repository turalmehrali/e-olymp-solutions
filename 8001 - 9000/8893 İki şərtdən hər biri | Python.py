
n = int(input())
b = False

if n % 3 == 0 and n % 2 == 0 and len(str(abs(n))) == 2:
	b = True

if b:
	print("YES")

if not b:
	print("NO")

