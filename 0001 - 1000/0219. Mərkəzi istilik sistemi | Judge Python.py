a, b, c, d = input().split()

k = float(a) * float(b) * float(c) / float(d)

if k % 1.0 == 0:
    answer = float(a) * float(b) * float(c) / float(d)

else:
    answer = float(a) * float(b) * float(c) / float(d) + 1

print(int(answer))
