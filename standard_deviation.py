# calculate standard deviation of atleats 5 no.

import math

sum = 0
sum_sqr = 0
n = 0
numbers = []

# Input numbers
while True:
    data = int(input("Enter a number: "))
    numbers.append(data)
    n += 1
    sum += data
    sum_sqr += data ** 2
    next_input = input("Wish to enter more numbers? (y/n): ")
    if next_input == "n":
        break

# Ensure at least 5 numbers are entered
if n < 5:
    print('Please enter at least 5 numbers')
else:
    mean = sum / n
    variance = (sum_sqr - (sum ** 2 / n)) / (n - 1)
    sd = math.sqrt(variance)
    print('The standard deviation of the entered numbers is:', sd)
