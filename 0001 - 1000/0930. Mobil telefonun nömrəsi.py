
nomre = input()
reqemler = '0123456789'
say = 0
cavab = []

for i in reqemler:
    if i not in nomre:
        say += 1
        cavab.append(i)


print(say)
print(*cavab, end='')
