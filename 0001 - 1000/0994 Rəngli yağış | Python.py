n = int(input())
G = [[int(i) for i in input().split()]for j in range(n)]
saygac = 0 
input()
R =[int (r) for r in input().split()]
for i in range(n):
    for j in range(i, n):
        if G[i][j]==1:
            if R[i]!=R[j]:
                saygac = saygac + 1
print(saygac)
