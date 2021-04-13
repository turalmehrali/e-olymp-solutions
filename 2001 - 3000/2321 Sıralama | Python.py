n=int(input())
m=input().split()
for j in range(n-1):
    for i in range(n-1):
        if int(m[i+1])<int(m[i]):
           c=m[i]
           m[i]=m[i+1]
           m[i+1]=c
for i in range(n):
    print(int(m[i]),end=' ')
