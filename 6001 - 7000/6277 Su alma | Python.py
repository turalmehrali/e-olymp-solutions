n=int(input())
count=0
n=n*100
while n>=120:
   count+=n//120
   n=(n//120)*20+n%120
print(count)
