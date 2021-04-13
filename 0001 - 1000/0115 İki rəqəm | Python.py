n=int(input())
if n==1:
   print(2)
elif n==2:
   print(4)
else:
   a1=2
   a2=4
   for i in range(3,n+1):
       p=a1+a2
       a1=a2
       a2=p
   print(p)
