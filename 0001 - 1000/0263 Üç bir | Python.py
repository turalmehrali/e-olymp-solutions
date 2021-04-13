n=int(input())
if n==1:
   print(2)
elif n==2:
   print(4)
elif n==3:
   print(7)
else:
   a1=2
   a2=4
   a3=7
   for i in range(4,n+1):
       p=(a1+a2+a3)%12345
       a1=a2
       a2=a3
       a3=p
   print(p)
