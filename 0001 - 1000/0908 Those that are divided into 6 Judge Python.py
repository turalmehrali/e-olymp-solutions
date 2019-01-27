N = int(input())
ededler = [int(i) for i in input().split()]
cem = 0
say = 0
for j in ededler:
    if(j > 0 and j % 6 == 0):
        cem += j
        say += 1
print(say, cem)
