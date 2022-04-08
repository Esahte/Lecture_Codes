sum = 0
number = 0

while number < 20:
    number += 1
    if number == 10 or number == 15:
        continue
    sum += number
    print(number, " ", sum)
print("The number is", number)
print("The sum is", sum)
