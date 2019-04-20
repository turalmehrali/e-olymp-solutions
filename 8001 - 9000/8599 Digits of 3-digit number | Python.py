
n = int(input())

first_digit = n // 100
second_digit = n // 10 % 10
last_digit = n % 10

print(first_digit, second_digit, last_digit)
