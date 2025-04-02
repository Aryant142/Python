def countd(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count 

n = int(input('Enter a number: '))
original_n = n  
digit_count = countd(n)
sum = 0

# Reversing the number
while n > 0:
    y = n % 10  
    digit_count -= 1  
    sum += y * 10**digit_count  
    n //= 10  


if sum == original_n:
    print('The entered number is a palindrome.')
else:
    print('The entered number is not a palindrome.')
