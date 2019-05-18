
vedre = 0
gun = 0
say = int(input())
i = say

while(vedre <= 0.5):
    vedre = vedre + 1/i
    gun += 1
    i = i - 1

print(say - gun + 1)
