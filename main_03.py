'''
TODO za DZ
1.a. Kreirajte program koji omogucava korisniku unos naziva filomova koliko god to korisnik zeli.
        Nakon sto je unio sve zeljene filmove ispiste listu filmova, ali tako da su sortirani od A prema Z

movies = []
movie_id = 1

while True:

    movie = input('Upisite naziv filma: ')
    movies.append([movie_id, movie])
    movie_id += 1

    next_movie = input('Zelite li unijeti novi film? (da/ne): ')
    if next_movie.lower() != 'da':
        break


# Ispis liste filmova

# Trajno sortirati listu
# movies.sort()

# pomocu sorted(lista) funkcije dobit cemo sortiranu listu, ali cemo zadrzati originalni raspored elemenata u listi
for index, movie in enumerate(sorted(movies)):
    print(f'Naziv {index + 1}. filma: ID: {movie[0]}, NAZIV: {movie[1]}.')


               1         2         3         4         5         6
             0   1     0   1     0   1     0   1     0   1     0   1
movies = [ [0, 'r'], [1, 'u'], [2, 'a'], [3, 'm'], [4, 'f'], [5, 'c'] ]

movies[5] => [1, 'u']
movies[2][0] => 4
movies[2][1] => 'f'









1.b. Napravite slican zadataka prvom, ali u ovoj verziji neka bude unos playliste.
        Nakon unosa liste pjesama, onda ispisite listu, ali "shuffled".


import random as rnd


playlist = []

while True:

    song = input('Upisite naziv pjesme: ')
    playlist.append(song)

    next_song = input('Zelite li dodati novu pjesmu? (da/ne): ')
    if next_song.lower() != 'da':
        break


# Ispis liste pjesama
# pomocu rnd.shuffle(lista) funkcije unutar random modula, dobit cemo trajno promijesanu listu
rnd.shuffle(playlist)
for index, song in enumerate(playlist):
    print(f'Naziv {index + 1}. pjesme: {song}.')










2. Napišite program koji generira note akorda na osnovu početnog tona, odnosno note.
        POJAŠNJENJE
        Akord se sastoji od tri tona koji se mogu ponavljati.
        Durski akord čine: početni ton, 4. ton te 7. ton.
            Označava se samo velikim slovom početnog tona
            ili velikim slovom početnog tona uz dodatak dur (D ili D dur)

        Molski akord čine: poćetni ton, 3. ton te 7. ton.
            Označava se samo malim slovom početnog tona
            ili malim slovom početnog tona uz dodatak mol (d ili d mol)

        Glazbena abeceda počinje od C:
            C, C#, D, D#, E, F, F#, G, G#, A, A#, H

        Engleska oznaka za H ton je B tako da oni imaju A B C D E F G tonove

        Postoji pojašnjenje u teoriji glazbe zašto je prvi ton C,
        ali to sada nije važno.


        1. Korisnik upiste slovo tona na osnovu kojeg zeli da mu generirate akord
        2. Nakon toga program ispise naziv akorda:
            C (C dur): C E G
            c (c mol): C D# G

        3. Nakon toga pita korisnika zeli li generirati jos jedan akord.
'''

#           0    1     2     3    4    5    6     7    8     9    10    11
# tones = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']

while True:
    tones = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']

    for tone in tones:
        print(tone, end=' ')
    print()

    chord_note = input('Upisite notu za koju zelite generirati akord: ')
    chord_note = chord_note.upper()

    # lista.extend(nova_lista) - metoda koja listu prosiruje s novom listom
    #   tako da novu listu doda na kraj prve liste
    tones.extend(tones)
    chord_note_index = tones.index(chord_note)
    chord_note_third = tones[chord_note_index + 3]
    chord_note_fourth = tones[chord_note_index + 4]
    chord_note_seventh = tones[chord_note_index + 7]

    # Durski akord je pocetni ton pa 4 pa 7
    print(f'{chord_note}: {chord_note}, {chord_note_fourth}, {chord_note_seventh}')


    # Molski akord je pocetni ton pa 4 pa 7
    print(f'{chord_note.lower()} mol: {chord_note}, {chord_note_third}, {chord_note_seventh}')
    print()
    tones.clear()

    next_tone = input('Zelite li generirati novi akord? (da/ne): ')
    if next_tone.lower() != 'da':
        break










# Mario Vojić

lista_nota = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]

slovo_tona = input ('Unesite slovo tona: ')

for i in range(len(lista_nota)):
    if slovo_tona == lista_nota[i]:
        indeks = i
        break


dur_ton_I = ((indeks + 4) % 12)
dur_ton_II = ((indeks + 7) % 12)
mol_ton_I = ((indeks + 3) % 12)
mol_ton_II = ((indeks + 7) % 12)


print()
print (f'{lista_nota[indeks]} ({lista_nota[indeks]} dur): {lista_nota[indeks]} {lista_nota[dur_ton_I]} {lista_nota[dur_ton_II]} ')
print (f'{lista_nota[indeks]} ({lista_nota[indeks]} mol): {lista_nota[indeks]} {lista_nota[mol_ton_I]} {lista_nota[mol_ton_II]} ') 