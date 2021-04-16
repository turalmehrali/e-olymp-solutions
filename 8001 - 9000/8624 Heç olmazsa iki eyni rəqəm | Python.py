n=int(input())
a=n//10000
b=n//1000%10
c=n//100%10
d=n//10%10
e=n%10
if a==b or a==c or a==d or a==e or b==c or b==d or b==e or c==d or c==e or d==e:
    print("YES")
else:
    print("NO")
