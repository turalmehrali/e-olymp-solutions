n=int(input())
a=n//1000
b=n//100%10
c=n//10%10
d=n%10
if (a==b and c==d and a!=c) or (a==c and b==d and a!=b) or (a==d and b==c and a!=b):
    print("YES")
else:
    print("NO")
