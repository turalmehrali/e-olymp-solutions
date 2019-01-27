a, b, c = input().split()
if(int(a)**2 == int(b)**2 + int(c)**2 and int(a) < int(b) + int(c)):
    print("YES")
elif(int(b)**2 == int(a)**2 + int(c)**2 and int(b) < int(a) + int(c)):
    print("YES")
elif(int(c)**2  == int(a)**2 + int(b)**2 and int(c) < int(a) + int(b)):
    print("YES")
else:
    print("NO")
