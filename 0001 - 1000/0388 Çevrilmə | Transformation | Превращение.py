
n = int(input())
say = 0

while n > 1:
    if n % 2 == 0:
        n = n // 2
        say += 1

    else:
        n += 1
        say += 1


print(say)
