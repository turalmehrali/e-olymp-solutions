n=int(input())
a=[[int(i) for i in input().split()] for j in range(n)]
for i in range(1,n):
    a[i][0]+=a[i-1][0]
    a[i][-1]+=a[i-1][-1]
    for j in range(1,i):
        a[i][j]+=max(a[i-1][j],a[i-1][j-1])
print(max(a[-1]))
