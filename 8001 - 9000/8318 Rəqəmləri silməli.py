
n = input()
ededler = []

for i in n:
    if i != "3" and i != "9":
        ededler.append(i)


print(*ededler, sep="")



# variant 2


"""



n = input()
ededler = []

for i in n:
    if i == "9" or i == "3":
        pass
    else:
        ededler.append(i)


print(*ededler, sep="")


"""
