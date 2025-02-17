'''
TODO za DZ
1.a. Kreirajte program koji omogucava korisniku unos naziva filomova koliko god to korisnik zeli.
        Nakon sto je unio sve zeljene filmove ispiste listu filmova, ali tako da su sortirani od A prema Z
'''

movies = []
movie_id = 1

while True:

    movie = input('Upisite naziv filma: ')
    movies.append([movie_id, movie])
    movie_id += 1

    next_movie = input('Zelite li unijeti novi film? (dan/ne): ')
    if next_movie.lower() != 'da':
        break


# Ispis liste filmova

# Trajno sortirati listu
# movies.sort()

# pomocu sorted(lista) funkcije dobit cemo sortiranu listu, ali cemo zadrzati originalni raspored elemenata u listi
for index, movie in enumerate(sorted(movies)):
    print(f'Naziv {index + 1}. filma: ID: {movie[0]}, NAZIV: {movie[1]}.')


#                1         2         3         4         5         6
#              0   1     0   1     0   1     0   1     0   1     0   1
'''movies = [ [0, 'r'], [1, 'u'], [2, 'a'], [3, 'm'], [4, 'f'], [5, 'c'] ]

movies[5] => [1, 'u']
movies[2][0] => 4
movies[2][1] => 'f'
'''


'''
1.b. Napravite slican zadataka prvom, ali u ovoj verziji neka bude unos playliste.
        Nakon unosa liste pjesama, onda ispisite listu, ali "shuffled".


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