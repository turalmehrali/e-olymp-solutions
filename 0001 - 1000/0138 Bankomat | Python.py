a=[500,200,100,50,20,10]
n=int(input())
s=0
i=0
while n>=10:
    s=s+n//a[i]
    n=n%a[i]
    i=i+1
if n!=0:
    print(-1)
else:
    print(s)
