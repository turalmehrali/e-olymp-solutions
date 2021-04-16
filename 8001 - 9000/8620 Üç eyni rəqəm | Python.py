n=int(input())
a=n//1000
b=n//100%10
c=n//10%10
d=n%10
if (a==b==c and a!=d) or (a==c==d and a!=b) or (a==b==d and a!=c) or (b==c==d and a!=b):
    print("YES")
else:
    print("NO")
