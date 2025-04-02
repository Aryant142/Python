import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '<', '>']

password=[]

n=int(input("enter the number of digit of password "))
for i in range(int(n/2)):
    password+=random.choice(letters)
for i in range(int(n/2)):
    password+=random.choice(symbols)
for i in range(int(n/2)):  
    password+=random.choice(numbers)
print(f"your  password is : {password}")

 