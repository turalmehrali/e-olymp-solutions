
n = int(input())

eded1 = n // 10

eded2 = (n // 100) * 10 + n % 10

eded3 = n % 100

print(max(eded2, eded1, eded3))



