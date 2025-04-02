# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def primes_up_to_n(n):
#     return [num for num in range(2, n + 1) if is_prime(num)]

# n = int(input("Enter a number: "))
# print("Prime numbers up to", n, "are:", primes_up_to_n(n))



# def is_prime(number):
#     if number <= 1:
#         return False  # Numbers less than 2 are not prime
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False  # If divisible by any number other than 1 and itself, not prime
#     return True  # If no divisors found, it's prime

# # Example usage
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")
