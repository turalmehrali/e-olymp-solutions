faktorial = 1
reqem = int(input())

while (0 <=reqem <= 3000):

        for i in range(1, reqem + 1):
            faktorial = faktorial * i

        print(faktorial)
        break
