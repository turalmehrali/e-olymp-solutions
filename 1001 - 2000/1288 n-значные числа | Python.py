n,a,b=map(int,input().split())
if a==0 and b==0:
   print(0)
else:
   if  a==0 or b==0 or a==b:
        print(1,end="")
   else:
        print(2,end="")

   for i in range(n-1):
        print(0,end="")
