
led_counts = {
    "0": 6,
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6
}


n = input()
say = 0

for i in n:
    for j in led_counts.keys():
        if i == j:
            say += led_counts.get(j)


print(say)

