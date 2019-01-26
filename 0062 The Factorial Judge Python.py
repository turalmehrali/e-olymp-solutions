fact = 1
n = int(input())
for i in range(1, 2001):
    fact = fact * i
    if (fact == n):
        print(i)
        break
