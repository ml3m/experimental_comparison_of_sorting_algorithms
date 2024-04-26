import random


def generate_random_list(length):
    return [random.randint(0, 999999) for _ in range(length)]

# Generate a list with 10 random integers
random_list = generate_random_list(100)
print(random_list)
