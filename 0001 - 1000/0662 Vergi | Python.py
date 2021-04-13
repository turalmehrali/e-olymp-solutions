n=int(input())
vergi=n//100

if n%100!=0:
    vergi+=1
    
print(vergi)
