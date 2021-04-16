def funksiya(n):
    f=0
    for i in range(1,n+1):
        f=f+i
    return f

n=int(input())

if n==0:
    print('0')
elif n>0:
    cavab=funksiya(n)
    print(cavab)
