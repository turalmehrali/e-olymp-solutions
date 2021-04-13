n=int(input())
ededler=[int(i) for i in input().split()]
ededler.insert(0,ededler[n-1])
ededler.pop(-1)
print(*ededler[0:])
