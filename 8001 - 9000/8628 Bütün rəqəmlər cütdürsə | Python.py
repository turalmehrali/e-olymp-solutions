n=int(input())
a=n//1000
b=n//100%10
c=n//10%10
d=n%10

if (a%2==0 and b%2==0 and c%2==0 and d%2==0):
    print('YES')
else:
    print('NO')
