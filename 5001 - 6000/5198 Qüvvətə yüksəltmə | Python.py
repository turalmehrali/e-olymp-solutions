def power(x,y,z):
    if y == 0:
        return 1
    elif y%2 == 0:
        return power(((x%n)*(x%n))%n,y//2,n)%n
    else:
        return ((x%n)*(power(((x%n)*(x%n))%n,y//2,n))%n)%n

a,b,n=map(int,input().split())
d=power(a,b,n)
print(d)
