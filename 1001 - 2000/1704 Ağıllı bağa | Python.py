n,m=map(int,input().split())
a=[[1 for i in range(m)]for j in range(n)]
for i in range(1,n):
    for j in range(1,m):
        a[i][j]=a[i-1][j]+a[i][j-1]
print(a[n-1][m-1])
