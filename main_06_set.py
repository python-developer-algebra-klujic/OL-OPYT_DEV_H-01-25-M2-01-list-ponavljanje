# prazan set
numbers = set()
print(numbers)
print()

# predefinirani set
numbers = {1, 2, 3, 4, 5, 6, 6, 2, 5, 4}
print(numbers)

numbers.add(10)
numbers.add(11)
numbers.add(1)
print(numbers)

# Primjena seta
list_numbers = [1, 1, 1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 9, 9]
set_unique_numbers = set(list_numbers)
print(set_unique_numbers)

list_unique_numbers = list(set_unique_numbers)
# list_unique_numbers = [set_unique_numbers]

print(list_unique_numbers)
