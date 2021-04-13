n,m=map(int,input().split())
k=m//n
f=m%n
if f!=0:
    print(k+1)
else:
    print(k)
