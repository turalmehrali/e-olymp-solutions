n = input()
hasil = 1
cem = 0

for i in n:
    hasil = hasil*int(i)
    cem = cem + int(i)
cavab = hasil/cem
print("{0:.3f}".format(cavab))
