# Gra papier kamień nożyce

from random import*
gra = True

while gra:
    wybor = (input('papier/nożyce/kamień: '))
    losowa = randint(1, 3)

    if losowa == 1:
        print('papier')
        if wybor == 'papier':
            print('Remis!')
        elif wybor == 'kamień':
            print('Przegrałeś!')
            gra = False
        elif wybor == 'nożyce':
            print('Wygrałeś!')
            gra = False

    elif losowa == 2:
        print('nożyce')
        if wybor == 'papier':
            print('Przegrałeś!')
            gra = False
        elif wybor == 'kamień':
            print('Wygrałeś!')
            gra = False
        elif wybor == 'nożyce':
            print('Remis!')

    elif losowa == 3:
        print('kamień')
        if wybor == 'papier':
            print('Wygrałeś!')
            gra = False
        elif wybor == 'kamień':
            print('Remis!')
        elif wybor == 'nożyce':
            print('Przegrałeś!')
            gra = False

    if wybor != 'papier' and wybor != 'nożyce' and wybor != 'kamień':
        print('Albo papier albo nożyce albo kamień!')
