n, m = map(int,input().split())
T = [0 for i in range(n)]
for i in range(m):
    x, y = map(int,input().split())
    T[x-1]+=1
    T[y-1]+=1
for i in T:
    print(i)
