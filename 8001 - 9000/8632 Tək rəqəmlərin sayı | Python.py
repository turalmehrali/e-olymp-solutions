n=int(input())
say=0
for i in str(n):
    if int(i) % 2 != 0:
        say += 1
print(say)
