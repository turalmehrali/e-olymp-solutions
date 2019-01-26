
simmetriya_derecesi = 0
n = input()
a = len(n)
if(int(a) % 2 == 1):
    simmetriya_derecesi += 1
for i in range(0, int(a)//2):
    if(n[i] == n[a-(i+1)]):
        simmetriya_derecesi += 1
print(simmetriya_derecesi)
