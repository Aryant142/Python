import random

# Generate a random float between 0 and 1
print(random.random())

# Generate a random float between 1 and 10
print(random.uniform(1, 10))

# Generate a random integer between 1 and 10
print(random.randint(1, 10))

# Choose a random element from a list
my_list = [1, 2, 3, 4, 5]
print(random.choice(my_list))

# Shuffle a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

# Generate a random sample from a population
population = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample = random.sample(population, 5)
print(sample)

# Generate a random integer with a specified number of bits
print(random.getrandbits(4))

# Generate a random integer within a range
print(random.randrange(1, 10, 2))