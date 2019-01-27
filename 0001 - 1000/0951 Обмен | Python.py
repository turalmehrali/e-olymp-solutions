eded = int(input())
minlik = eded // 1000
yuzluk = eded // 100 % 10
onluq = eded // 10 % 10
teklik = eded % 10
cavab = minlik * 1000 + onluq * 100 + yuzluk * 10 + teklik

print(cavab)
