

numbers_1_to_50 = []
numbers_1_to_12 = []
wining_combination = []


for number in range(1, 51): # od 1 do 50 -> prvi broj je ukljucen, a zadnji nije i korak je predefiniran na 1
    numbers_1_to_50.append(number)

for number in range(1, 13): # od 1 do 12 -> prvi broj je ukljucen, a zadnji nije i korak je predefiniran na 1
    numbers_1_to_12.append(number)


for _ in range(5):
    number = numbers_1_to_50[15]
    wining_combination.append(number)


for _ in range(2):
    number = numbers_1_to_12[15]
    wining_combination.append(number)


# ispisati izvucene brojeve
print()
for i in range(7):
    if i == 6:
        print(f'{wining_combination[i]}')
    else:
        print(f'{wining_combination[i]}', end=', ')

print()
for index, number in enumerate(wining_combination):
    if index == 6:
        print(f'{number}')
    else:
        print(f'{number}', end=', ')
