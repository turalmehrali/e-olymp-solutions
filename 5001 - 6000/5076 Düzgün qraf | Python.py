MAX=110
n, m = map(int, input().split())
T=[0 for i in range(MAX)]

for i in range(m):
    a,b = map(int, input().split())
    T[a]+=1
    T[b]+=1

flag=0
for i in range(1, n):
    if T[i]!=T[i+1]:
        flag=1
if (flag==0):
    print('YES')
else:
    print('NO')
