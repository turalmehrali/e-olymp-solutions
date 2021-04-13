n=int(input())
a=[[int(i) for i in input()] for j in range (n)]
for i in range(1,n):
    a[0][i]+=a[0][i-1]
    a[i][0]+=a[i-1][0]
for i in range(1,n):
    for j in range(1,n):
        a[i][j]+=min(a[i-1][j],a[i][j-1])
a[n-1][n-1]=-1
i=j=n-1
while i!=0 and j!=0:
    if a[i][j-1] < a[i-1][j]:
        j=j-1
    else:
        i=i-1
    a[i][j]=-1
while i>=0:
    a[i][0]=-1
    i=i-1
while j>=0:
    a[0][j]=-1
    j=j-1
for i in range(n):
    for j in range(n):
        if a[i][j]==-1:
            print('#',end='')
        else:
            print('.',end='')
    print()
