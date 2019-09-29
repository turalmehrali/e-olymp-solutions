
n = input()
ededler = [int(i) for i in input().split()]
tekler = []
ind = 0

for i in ededler:
	if ind % 2 == 0:
		tekler.append(str(i))
	
	ind += 1

print(" ".join(tekler))

