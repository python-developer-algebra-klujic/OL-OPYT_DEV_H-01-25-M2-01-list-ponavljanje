# Aplikaicja za proricanje buducnosti
# Koristimo tri liste u kojima imamo nekoliko subjekata, akcija i zakljucaka
# Koristeci random modul mozemo iz svake liste izvuci jednu vrijednost
# te ju spojiti u jednu recenicu.

# DONE Doradite ovaj program tako da omogucava generiranje prorocanstava
# sve dok god to korisnik zeli. Dodajte da se prije svakog ispisa ocisti ekran
# a upit zeli li korisnik ponoviti generiranje da bude ispod i odmaknuto dva prazna reda

import random as rnd
import os


subject = [
'Uskoro ćeš ',
'U bliskoj budućnosti ćeš ',
'Očekuj da će ti ',
'Sudbina ti donosi ',
'Bit ćeš iznenađen/a kada ',
'Tvoje srce će osjetiti ',
'Velika promjena te čeka kada ',
'Pripremi se jer ćeš ',
'Neočekivani događaj će ti ',
'Zvijezde su ti naklonjene i uskoro ćeš ',
'Sudbina je već odlučila da ćeš ',
'Netko iz tvoje prošlosti će ti ',
'Putovanje koje uskoro dolazi će ti ',
'Tvoje sposobnosti će te dovesti do ',
'Vrijeme je da otkriješ svoju unutarnju snagu i ',
'Snaga tvoje volje će ti pomoći da ',
'Svemir ti šalje znakove da trebaš ',
'Promjena na koju čekaš će se dogoditi kad ',
'Netko koga nisi očekivao/la će ti '
]
action = [
'pronaći skriveni talent.',
'upoznati osobu koja će ti promijeniti život.',
'dobiti priliku koju ne smiješ propustiti.',
'otkriti tajnu koju nitko ne zna.',
'doživjeti nevjerojatnu avanturu.',
'napraviti hrabru odluku.',
'suočiti se s izazovom koji će te osnažiti.',
'naučiti nešto što će ti promijeniti perspektivu.',
'primiti neočekivane vijesti.',
'osjetiti duboku povezanost s nekim posebnim.',
'pronaći odgovor koji već dugo tražiš.',
'shvatiti da je pravi trenutak za novi početak.',
'otkriti nešto novo o sebi.',
'suočiti se s prošlošću i krenuti dalje.',
'pronaći novi smisao u stvarima koje voliš raditi.',
'dobiti priznanje koje zaslužuješ.',
'shvatiti koliko vrijediš.',
'neočekivano dobiti financijsku korist.',
'biti u centru pažnje zbog nečega važnog.',
'otkriti da netko u tajnosti misli na tebe.',
'napokon ostvariti dugo sanjani cilj.',
'postići nešto za što nisi vjerovao/la da možeš.',
'pronaći sreću na mjestu na kojem najmanje očekuješ.',
'dobiti inspiraciju koja će promijeniti tvoj život.',
'sresti starog prijatelja koji će imati važnu poruku za tebe.',
'napraviti važnu odluku koja će promijeniti tvoj smjer.',
'pronaći neočekivanu priliku za novi početak.'
]
conclusion = [
'Iskoristi tu priliku mudro!',
'Nemoj se bojati, jer će sve ispasti dobro.',
'Budi hrabar/ra i slušaj svoje srce.',
'Samo onaj tko riskira, pobjeđuje!',
'Bit ćeš nagrađen/a za svoj trud.',
'Ponekad je potrebno napraviti korak unatrag da bi se išlo naprijed.',
'Vjeruj u proces i ne odustaj!',
'Sreća je na tvojoj strani.',
'Ne boj se promjena, one su tvoj put prema boljem.',
'Kad zatvoriš jedna vrata, druga će se otvoriti.',
'Ne dopusti strahu da te spriječi u ostvarivanju snova.',
'Oslobodi se prošlosti i prigrli budućnost.',
'Uživaj u putovanju, a ne samo u cilju.',
'Ne osvrći se unatrag, jer ono najbolje tek dolazi.',
'Ponekad su izazovi znak da si na pravom putu.',
'Poslušaj svoju intuiciju – ona zna put.',
'Svaka prepreka je prilika za rast.',
'Najveće nagrade dolaze onima koji vjeruju u sebe.',
'U svakoj situaciji pronađi razlog za osmijeh.',
'Zadrži pozitivan stav i sve će doći na svoje mjesto.',
'Život ti priprema nešto predivno – samo budi strpljiv/a.',
'Tvoje srce već zna odgovor, samo ga moraš poslušati.',
'Prilika će se pojaviti kada najmanje očekuješ.',
'Samo hrabro naprijed – tvoje vrijeme dolazi!'
]


while True:
    os.system('cls')

    random_subject = rnd.choice(subject)
    random_action = rnd.choice(action)
    random_conclusion = rnd.choice(conclusion)

    print()
    print('Baba Vanga: Bogovi imaju poruku za tebe:')
    print(f'{random_subject} {random_action} {random_conclusion}')
    print('\n\n')

    novo_prorocanstvo = input('Želite li novo prorocanstvo (Da/Ne)? ')
    if novo_prorocanstvo.lower() == 'ne':
        break
