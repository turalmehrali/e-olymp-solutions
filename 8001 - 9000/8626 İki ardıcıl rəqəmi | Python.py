n=int(input())
a=n//1000
b=n//100%10
c=n//10%10
d=n%10

if (a==3 and b==7) or (b==3 and c==7) or (c==3 and d==7):
    print('YES')
else:
    print('NO')
