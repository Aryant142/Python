n = int(input('Enter a three-digit number: '))
total_sum = 0
a = n

while a > 0:
    x = a % 10  # Get the last digit
    total_sum += x ** 3  # Cube the digit and add to sum
    a //= 10  # Perform integer division to remove the last digit

# Check if the sum of cubes is equal to the original number
if total_sum == n:
    print(f'{n} is an Armstrong number.')
else:
    print(f'{n} is not an Armstrong number.')
 