l, k = input().split()
say = 0

while (float(l) > 1):
    l = float(l) / int(k)
    if(l > 1):
        say += 1

print(say)
