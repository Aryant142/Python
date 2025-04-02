def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd_value = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is", gcd_value)

# import math

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# gcd = math.gcd(a, b)
# lcm = (a * b) // gcd  # Formula: LCM(a, b) = (a × b) / GCD(a, b)

# print(f"GCD of {a} and {b} is: {gcd}")
# print(f"LCM of {a} and {b} is: {lcm}")

