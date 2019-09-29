
n = input()
ededler = [int(i) for i in input().split()]
netice = []
ind = 1

for i in ededler[1:]:
	if i > ededler[ind - 1]:
	    netice.append(str(i))
	
	ind += 1

print(" ".join(netice))

