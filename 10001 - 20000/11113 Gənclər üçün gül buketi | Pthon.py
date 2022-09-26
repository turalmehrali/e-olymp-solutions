n,m = map(int, input().split())
if n==0 or m==0:
    print(0)
else:
    if n<m//2:
        print(n)
    elif m<n//2:
        print(m)
    else:
        print((n+m)//3)
