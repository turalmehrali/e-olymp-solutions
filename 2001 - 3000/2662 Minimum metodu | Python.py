n=int(input())
a=[int(i) for i in input().split()]
k=a[0]
say=0
for i in range(n-1):
    m=i
    for j in range(i+1,n):
        if a[m]>a[j]:
             m=j
    a[m],a[i]=a[i],a[m]
    if m!=i and (a[m]==k or a[i]==k):
        say+=1
print(say)
