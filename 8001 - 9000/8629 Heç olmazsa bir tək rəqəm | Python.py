n=int(input())
a=n//1000
b=n//100%10
c=n//10%10
d=n%10

if (a%2==1 or b%2==1 or c%2==1 or d%2==1):
    print('YES')
else:
    print('NO')
