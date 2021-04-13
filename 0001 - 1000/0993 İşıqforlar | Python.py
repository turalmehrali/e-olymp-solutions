n,m=input().split()
n=int(n)
m=int(m)
lt=[]
for y in range(m):
    a,b=input().split()
    a=int(a)
    b=int(b)
    lt.append(a)
    lt.append(b)
for s in range(1,n+1):
    print(lt.count(s),end =  " ")
