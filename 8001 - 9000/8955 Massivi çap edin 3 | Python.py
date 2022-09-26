n=int(input())
mass=[int(i) for i in input().split()]
k=0

for i in mass:
    if i>0:
        k+=1

if k==0:
    print("NO")
else:
    print(k)
    for i in mass:
        if i>0:
            print(i)
