e,f,c=map(int,input().split())
cem=0
n=e+f

while n>=c:
    q=n%c
    cem+=n//c
    n=n//c+q

print(cem)
