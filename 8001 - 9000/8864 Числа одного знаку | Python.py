n, m = input().split()

if (int(n) > 0 and int(m) > 0) or (int(n) < 0 and int(m) < 0):
	print("1")

elif (int(n) > 0 and int(m) < 0) or (int(n) < 0 and int(m) > 0):
	print("0")
