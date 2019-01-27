n = input()
ededler = [float(j) for j in input().split()]
say = 1
for i in ededler:
    say += 1
    if(float(i) <= 2.5):
        print(say - 1, "{0:.2f}".format(float(i)))
        break
    if(say == int(n) + 1):
        print("Not Found")
