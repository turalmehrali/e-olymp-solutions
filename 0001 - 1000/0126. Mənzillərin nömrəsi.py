a, b, c, d = input().split()
e = int(d)
nomre = 1

while e > int(a) / int(b):
    e -= int(a) / int(b)
    nomre += 1

print(nomre, end=' ')
e = d
nomre = 1

while int(d) > int(a) / (int(b) * int(c)):
    d = int(d) -  (int(a) / (int(b) * int(c)))
    nomre += 1
    if nomre == int(c) + 1:
        nomre = 1

print(nomre)
