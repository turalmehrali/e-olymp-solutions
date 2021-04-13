n = int(input())

G=[]

for i in range(n):
 temp =[int(g) for g in input().split()]
 G.append(temp);
cem = 0 
for g in G:
 cem += sum(g)
print(cem//2)
