n=int(input())
a=[[int(i) for i in input().split()]for j in range(n)]
for i in range(n):
     for j in range(n):
         if a[i][j]==1:
             for k in range(n):
                 if a[j][k]==1 and a[i][k]==0:
                     print('NO')
                     exit()
print('YES')
