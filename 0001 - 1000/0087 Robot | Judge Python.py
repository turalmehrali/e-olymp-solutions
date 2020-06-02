
commands = input()
coordinates = [0]
s = 0

for i in commands:
    if i == "R":
        s += 1
        coordinates.append(s)

    elif i == "L":
        s -= 1
        coordinates.append(s)

print(len(set(coordinates)))


