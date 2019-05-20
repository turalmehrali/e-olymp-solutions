
n = input()
emel_sayi = 0

if n[0] == "-":
    emel_sayi = emel_sayi - 1

if n[0] == "+":
    emel_sayi = emel_sayi - 1

for i in n:

    if i == "+":
        emel_sayi = emel_sayi + 1
    if i == "*":
        emel_sayi = emel_sayi + 1
    if i == "-":
        emel_sayi = emel_sayi + 1

print(emel_sayi)
