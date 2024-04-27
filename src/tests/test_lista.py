import random


def generate_random_list(length):
    """the function that generates a list with random number from range (0, 999999), assuring a correct testing on totally random numbers"""
    return [random.randint(0, 999999) for _ in range(length)]


lista = generate_random_list(10)
print(lista)

lista.sort()
print(lista)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
