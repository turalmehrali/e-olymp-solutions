n=int(input())
a=[int(i) for i in input().split()]
for i in range(1,n):
    key=a[i]
    j=i
    while j>0 and key<a[j-1]:
        j=j-1
    if j!=i:
        a.pop(i)
        a.insert(j,key)
        print(*a)
