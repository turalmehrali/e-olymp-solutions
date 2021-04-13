n,m=map(int,input().split())
A=[[0]*n for i in range(n)]
flag=0
for i in range(m):
    x,y=map(int,input().split())
    A[x-1][y-1]+=1
    if A[x-1][y-1]>1:
        flag=1
        break
print('YES' if flag else 'NO')
