n=int(input())
sablon=[[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print("*", end="")
        else:
            print(end=" ")
    print()
