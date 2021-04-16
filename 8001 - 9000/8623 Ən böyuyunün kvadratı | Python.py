n=int(input())
a=n//100
b=n//10%10
c=n%10
if a>=b>=c:
   y=100*a+10*b+c
elif a>=c>=b:
   y=100*a+10*c+b
elif b>=a>=c:
   y=100*b+10*a+c
elif b>=c>=a:
   y=100*b+10*c+a
elif c>=a>=b:
   y=100*c+10*a+b
else:
   y=100*c+10*b+a
print(y**2)
