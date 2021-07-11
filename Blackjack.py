# Blackjack

from random import*

gra = True
grakomputer = 1
dobieranie = 1
koniec = 1
suma = 0
sumakomputer = 0
wybor = 1
d = 0
a1 = 0
a2 = 0
gracz = 0
komputer = 0

while gra:
    losowa = randint(2, 14)
    losowakomputer = randint(2, 14)
    losowakopia = losowa
    losowakomputerkopia = losowakomputer

    if dobieranie == 1:
        if losowa == 11:
            losowa = 10
            print('Wyciągnąłeś waleta! (10)')
        if losowa == 12:
            losowa = 10
            print('Wyciągnąłeś damę! (10)')
        if losowa == 13:
            losowa = 10
            print('Wyciągnąłeś króla! (10)')
        if losowa == 14:
            losowa = 11
            a1 = a1 + 1
            print('Wyciągnąłeś asa! (11)')

    # Wypisywanie i obliczanie sumy wartości kart gracza oraz asów:
    if dobieranie == 1 and losowakopia < 11:
        print('Wyciągnąłeś: ', losowa)
    if dobieranie == 1:
        suma = suma + losowa
    if suma > 21 and a1 == 1:
        suma = suma - 10

    # Sprawdzanie czy nie wyciągnąłeś zbyt dużo albo nie masz 2 asów:
    if suma > 21:
        d = 0
        koniec = 0
        gra = False
        break
    if a1 == 2:
        d = 1
        koniec = 0
        gra = False
        break

    if grakomputer == 1:
        if losowakomputer == 11:
            losowakomputer = 10
            print('Komputer wyciągnął waleta! (10)')
        if losowakomputer == 12:
            losowakomputer = 10
            print('Komputer wyciągnął damę! (10)')
        if losowakomputer == 13:
            losowakomputer = 10
            print('Komputer wyciągnął króla! (10)')
        if losowakomputer == 14:
            losowakomputer = 10
            a2 = a2 + 1
            print('Komputer wyciągnął asa! (11)')

    # Wypisywanie i obliczanie sumy wartości kart komputera oraz asów:
    if grakomputer == 1 and losowakomputerkopia < 11:
        print('Komputer wyciągną: ', losowakomputer)
    if grakomputer == 1:
        sumakomputer = sumakomputer + losowakomputer
    if sumakomputer > 21 and a2 == 1:
        sumakomputer = sumakomputer - 10

    # Sprawdzanie czy komputer nie wyciągnął zbyt dużo albo nie ma 2 asów:
    if dobieranie == 0 and sumakomputer > suma:
        d = 0
        koniec = 0
        gra = False
        break
    if a2 == 2:
        d = 0
        koniec = 0
        gra = False
        break
    if suma == 21:
        dobieranie = 0
    if sumakomputer == 21:
        grakomputer = 0
    if sumakomputer > 21:
        d = 1
        koniec = 0
        gra = False
        break
    if dobieranie == 0 and grakomputer == 0:
        gra = False
        break

    # Wypisywanie wyniku rundy:
    print('\nSuma twoich liczb wynosi: ', suma)
    print('Suma liczb komputera wynosi: ', sumakomputer)

    if dobieranie == 1:
        wybor = (input('\nDobierz (napisz cokolwiek) albo stop (stop): '))
        print('\n-----------------------\n')
    if wybor == 'stop':
        dobieranie = 0

    # Sztuczna inteligencja komputera:
    if sumakomputer > suma and dobieranie == 0:
        gra = False
    elif suma > sumakomputer and grakomputer == 1:
        grakomputer = 1
    elif sumakomputer > 16:
        grakomputer = 0

    if dobieranie == 0 and grakomputer == 0:
        gra = False


# Końcowy wynik gry:
print('\n-----------------------')
if a1 == 2:
    print('\nWyrzuciłeś blackjacka!')
    print('Suma liczb komputera wynosi: ', sumakomputer)
elif a2 == 2:
    print('\nSuma twoich liczb wynosi: ', suma)
    print('Komputer wyrzucił blackjacka!')
else:
    print('\nSuma twoich liczb wynosi: ', suma)
    print('Suma liczb komputera wynosi: ', sumakomputer)

if koniec == 0:
    if sumakomputer > 21:
        print('\nWygrałeś!')
    elif suma > 21:
        print('\nPrzegrałeś!')
    elif d == 0:
        print('\nPrzegrałeś!')
    elif d == 1:
        print('\nWygrałeś!')
    elif d == 2:
        print('\nRemis!')

elif koniec == 1:
    gracz = 21 - suma
    komputer = 21 - sumakomputer
    if gracz == komputer:
        print('\nRemis!')
    elif gracz < komputer:
        print('\nWygrałeś!')
    else:
        print('\nPrzegrałeś!')

# gracz = 21 - suma
# komputer = 21 - sumakomputer
# if d == 1 or sumakomputer > 21 or gracz > komputer and gracz < 22:
#     print('\nWygrałeś!')
# elif d == 0 or suma > 21 or komputer > gracz:
#     print('\nPrzegrałeś!')
# elif d == 2 or gracz == komputer:
#     print('\nRemis!')
