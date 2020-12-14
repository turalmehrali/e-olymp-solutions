
n = int(input())
b = False
if n < 0:
	b = False

for i in range(0, n):
	kv = 10 ** i
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
  
  
  
