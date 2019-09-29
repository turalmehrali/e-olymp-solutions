
n = input()
ededler = [int(i) for i in input().split()]
boyuk = max(ededler)
say = 0

for i in ededler:
	if i == boyuk:
	    say += 1

print(say)

