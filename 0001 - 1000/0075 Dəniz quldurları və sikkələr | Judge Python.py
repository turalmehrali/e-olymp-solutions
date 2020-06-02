
a, m = input().split()
a = int(a)
m = int(m)
say = 0
cem = 0

while True:

    if cem + a * 2 == m:
        say += 1
        break

    cem += a
    a += 1
    say += 1

print(say)
