a, b, c = input().split()
if(int(a) %2 == 0 and int(b) %2 == 0 and int(c) %2 == 0):
    print("NO")
elif(int(a) %2 != 0 and int(b) %2 != 0 and int(c) %2 != 0):
    print("NO")
elif(int(a) %2 == 0 and int(b) %2 != 0 and int(c) %2 != 0):
    print("YES")
elif(int(a) %2 == 0 and int(b) %2 == 0 and int(c) %2 != 0):
    print("YES")
elif(int(a) %2 == 0 and int(b) %2 != 0 and int(c) %2 == 0):
    print("YES")
elif(int(a) %2 != 0 and int(b) %2 == 0 and int(c) %2 == 0):
    print("YES")
elif(int(a) %2 != 0 and int(b) %2 != 0 and int(c) %2 == 0):
    print("YES")
elif(int(a) %2 != 0 and int(b) %2 == 0 and int(c) %2 != 0):
    print("YES")
