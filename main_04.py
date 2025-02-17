# Slice notacija
'''
Podsjentik
       uklj. isklj. value=1
range(start, stop, step)
range(10) -> od 0 do 9

indeksi  0  1  2  3  4  5  6  7  8
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista[0] -> vratit ce vrijednost 1

slice notacija:
lista[start : stop : step]

primjer
lista[1 : 5 : 2] -> vratit ce elemente od indeksa 1 do indeksa 5 (nije ukljuceno), svaki drugi

indeksi          1  2  3  4  5
                [2,  , 4,  ,  ] -> [2, 4]

'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
part_of_numbers = numbers[1 : 5 : 2]

print(numbers)
print(part_of_numbers)


copy_of_numbers = numbers[ : : ]
print(copy_of_numbers)

desc_sorted_numbers = numbers[ : : -1]
print(desc_sorted_numbers)


# Zadatak Generirajte listu brojeva od 1 do 100
#   te u novu listu kopirajte brojeve od 20 do 45, ali svaki 5.
numbers = []

for i in range(1, 101):
    numbers.append(f'Broj: {i}')

new_list = numbers[ 19 : 45 : 5 ]
print(new_list)

new_list = numbers[ 44 : 20 : -5 ]
print(new_list)
