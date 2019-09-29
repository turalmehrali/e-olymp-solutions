
n = input()
ededler = [int(i) for i in input().split()]
or_cem = 0
or_say = 0
cem = 0
say = 0

for i in ededler:
    or_cem += i
    or_say += 1

ededi_orta = or_cem / or_say

for i in ededler:
    if i > ededi_orta:
        cem += i
        say += 1

print(cem, say)

