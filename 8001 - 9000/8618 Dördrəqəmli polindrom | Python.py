n=int(input())
a=n//1000
b=n//100%10
c=n//10%10
d=n%10
if a==d and b==c:
    print("YES")
else:
    print("NO")
