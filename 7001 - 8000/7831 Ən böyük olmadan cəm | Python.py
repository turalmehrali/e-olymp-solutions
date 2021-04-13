n=int(input())
massiv=[int(i) for i in input().split()]
cem=0
for i in massiv:
    if i<max(massiv):
        cem+=i
print(cem)
