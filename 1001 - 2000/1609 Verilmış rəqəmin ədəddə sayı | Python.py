n=abs(int(input()))
a=int(input())
say=0

while n>0:
    m=n%10
    if m==a:
        say+=1
    n=n//10
print(say)
