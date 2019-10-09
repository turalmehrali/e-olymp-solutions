
n = int(input())
b = False

if (n > 0 or n % 2 == 0) and (n < 0 or n % 2 != 0):
	b = True

if b:
	print("YES")

if not b:
	print("NO")

