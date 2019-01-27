eded = 2
a = input()
b = ""
for n in range(1, 1001):
    eded = 2 ** n
    b += str(eded)
    if(a == b):
        print(n)
        break
