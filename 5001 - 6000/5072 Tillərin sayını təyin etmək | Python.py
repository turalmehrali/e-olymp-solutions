n=int(input())
A=[[int(i) for i in input().split()]for j in range(n)]
S=0
for i in range(n):
    S+=sum(A[i])
print(S)
