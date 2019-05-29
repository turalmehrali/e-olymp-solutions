n = int(input())
sehife = 0
a = 9
b = 1
while True:
    if n <= b * a:
        if n % b != 0:
            print("0")
            break

        sehife += n / b
        print(int(sehife))
        break

    n -= a * b
    sehife += a
    a *= 10
    b += 1
