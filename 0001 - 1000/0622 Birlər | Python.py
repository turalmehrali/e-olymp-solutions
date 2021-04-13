
n = int(input())

ikilik = bin(n)

say = 0

for i in str(ikilik):
    if i == "1":
        say += 1

print(say)
