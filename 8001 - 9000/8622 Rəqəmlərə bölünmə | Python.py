n=int(input())
a=n//1000
b=n//100%10
c=n//10%10
d=n%10
if a!=0 and b!=0 and c!=0 and d!=0 and n%a==0 and n%b==0 and n%c==0 and n%d==0:
    print("YES")
else:
    print("NO")
