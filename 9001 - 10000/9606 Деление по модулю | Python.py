def powmod(x,n,m):
    if n == 0:
        return 1
    if n % 2 == 0:
        return powmod((x*x)%m,n//2,m)
    return (x*powmod(x,n-1,m))%m

a,b,n=map(int,input().split())
y=powmod(b,n-2,n)
x=(a*y)%n 
print(x)
if (b*x)%n!=a:
    print("error")
