n=int(input())
if n<0:
    n=-n
a=n%10
while n>=10:
    n=n//10
print(n+a)
