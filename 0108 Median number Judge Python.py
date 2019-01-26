a, b, c = input().split()

if(abs(int(a)) < 1000 and abs(int(b)) < 1000 and abs(int(c)) < 1000):
    if(int(a) < int(b) < int(c) or int(c) < int(b) < int(a)):
        print(b)
    elif(int(a) < int(c) < int(b) or int(b) < int(c) < int(a)):
        print(c)
    elif(int(b) < int(a) < int(c) or int(c) < int(a) < int(b)):
        print(a)
