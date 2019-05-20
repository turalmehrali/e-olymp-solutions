n = input()
ededler = [float(i) for i in input().split()]
cem = 0
say = 0

for j in ededler:
    if j > 0:
        cem += j
        say += 1
if say == 0:
    print("Not Found")

else:
    print('{0:.2f}'.format(cem / say))
