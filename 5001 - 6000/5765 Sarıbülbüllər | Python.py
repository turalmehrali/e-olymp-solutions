n,k=map(int,input().split())

f=n//k
s=n%k

if s!=0:
    min=f+1
    max=n-(k-1)
else:
    min=f
    max=n-(k-1)

print(min,max)
