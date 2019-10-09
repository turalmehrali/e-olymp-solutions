
n = int(input())
b = False

if n > 0 and len(str(abs(n))) == 3:
	b = True

if n % 2 != 0:
	b = True

if b:
	print("YES")

if not b:
	print("NO")

