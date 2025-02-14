import random


numbers_1_to_50 = []
numbers_1_to_12 = []
wining_combination = []


for number in range(1, 51): # od 1 do 50 -> prvi broj je ukljucen, a zadnji nije i korak je predefiniran na 1
    numbers_1_to_50.append(number)

for number in range(1, 13): # od 1 do 12 -> prvi broj je ukljucen, a zadnji nije i korak je predefiniran na 1
    numbers_1_to_12.append(number)


# TODO DZ - Prepraviti ovo rjesenje tako da se koristi .pop() metoda na listi
#   list.pop(index) vrati vrijednost iz liste na indeksu index i obrise taj element u listi
# for _ in range(5):
while len(wining_combination) < 5:
    random_number = random.randint(0, 49)
    number = numbers_1_to_50[random_number]

    if number not in wining_combination:
        wining_combination.append(number)


# for _ in range(2):
while len(wining_combination) < 7:
    random_number = random.randint(0, 11)
    number = numbers_1_to_12[random_number]

    if number not in wining_combination:
        wining_combination.append(number)


# ispisati izvucene brojeve
print()
for i in range(7):
    if i == 6:
        print(f'{wining_combination[i]}')
    elif i == 5:
        print(f'{wining_combination[i]}', end=', ')
    elif i == 4:
        print(f'{wining_combination[i]}')
    else:
        print(f'{wining_combination[i]}', end=', ')

print()
for index, number in enumerate(wining_combination):
    if index == 6:
        print(f'{number}')
    elif index == 5:
        print(f'{number}', end=', ')
    elif index == 4:
        print(f'{number}')
    else:
        print(f'{number}', end=', ')
