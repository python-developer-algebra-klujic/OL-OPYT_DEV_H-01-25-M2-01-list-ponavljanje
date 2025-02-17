# Tuple ili n-terac
import random as rnd


# PI = 3,14 # Ako korisstimo zarez - > Python ce generirati tuple (3, 14)
PI = 3.14

r = 10
O = 2 * r * PI

print(f'Opseg kruga radijusa {r} cm je {O:.2f} cm.')
print()


# numbers = (1, 2, 3, 4, 5)
numbers = 1, 2, 3, 4, 5
print(numbers)

list_of_numbers = list(numbers)
rnd.shuffle(list_of_numbers)

numbers = tuple(list_of_numbers)
print(numbers)
