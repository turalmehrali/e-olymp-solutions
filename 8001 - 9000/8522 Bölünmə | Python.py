a,b=map(int,input().split())

if a%b!=0:
    print(a//b, a%b)
else:
    print('Divisible')
