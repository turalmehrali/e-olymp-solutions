
a, b, x, y, z = input().split()

if 0 < int(a) < 10 and 0 < int(b) < 10 and 0 < int(x) < 10 and 0 < int(y) < 10 and 0 < int(z) < 10:
    if int(x) < int(a) and int(y) < int(b):
        print("1")

    elif int(y) < int(a) and int(x) < int(b):
        print("1")

    elif int(x) < int(a) and int(z) < int(b):
        print("1")

    elif int(z) < int(a) and int(x) < int(b):
        print("1")

    elif int(y) < int(a) and int(z) < int(b):
        print("1")

    elif int(z) < int(a) and int(y) < int(b):
        print("1")

    else:
        print("0")
