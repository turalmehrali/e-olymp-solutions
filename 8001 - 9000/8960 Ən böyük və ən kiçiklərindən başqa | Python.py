n=int(input())
array=[int(i) for i in input().split()]

summ=0
maxx=max(array)
minn=min(array)

for i in array:
    if i!=maxx and i!=minn:
        summ+=i
        
print(summ)
