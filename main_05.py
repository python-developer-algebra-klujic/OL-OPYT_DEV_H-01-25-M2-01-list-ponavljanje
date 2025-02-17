# List comprehension
# Klasicni nacin
numbers = []
for i in range(10):
    numbers.append(i)
print(numbers)

# Comprehension nacin
numbers = [i for i in range(10)]
print(numbers)



numbers = [i for i in range(20) if i % 2 == 0]
print(numbers)

numbers = []
for i in range(20):
    if i % 2 == 0:
        numbers.append(i)
print(numbers)



# Primjer iz prakse cisti ekran terminala na Windows i Linux OS-u
import os
# os.system('cls') -> samo za Windows
os.system('cls' if os.name == 'nt' else 'clear')
