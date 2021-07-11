# Oczko – prosta gra karciana, polegająca na dobieraniu kolejnych kart dotąd, aby
# osiągnąć wartość liczbową posiadanych kart jak najbliższą (ale nie większą niż) 21. Gracz
# otrzymuje kolejne karty z talii dotąd, aż sam zdecyduje, że nie chce już więcej kart, lub
# otrzyma wynik 21 lub większy. Suma większa lub równa 22 oznacza przegraną.
# Wyjątkiem od tej reguły jest perskie oczko (dwa asy). Perskie oczko zawsze oznacza
# wygraną. W oczko gra się talią od 2 do asa.

# Gra w oczko Wersja 1.0

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
            losowa = 2
            print('\nWyciągnąłeś waleta! (2)')
        if losowa == 12:
            losowa = 3
            print('\nWyciągnąłeś damę! (3)')
        if losowa == 13:
            losowa = 4
            print('\nWyciągnąłeś króla! (4)')
        if losowa == 14:
            losowa = 11
            a1 = a1 + 1
            print('\nWyciągnąłeś asa! (11)')

    # Wypisywanie i obliczanie sumy wartości kart gracza:
    if dobieranie == 1 and losowakopia < 11:
        print('\nWyciągnąłeś: ', losowa)
    if dobieranie == 1:
        suma = suma + losowa

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
            losowakomputer = 2
            print('Komputer wyciągnął waleta! (2)')
        if losowakomputer == 12:
            losowakomputer = 3
            print('Komputer wyciągnął damę! (3)')
        if losowakomputer == 13:
            losowakomputer = 4
            print('Komputer wyciągnął króla! (4)')
        if losowakomputer == 14:
            losowakomputer = 11
            a2 = a2 + 1
            print('Komputer wyciągnął asa! (11)')

    # Wypisywanie i obliczanie sumy wartości kart komputera:
    if grakomputer == 1 and losowakomputerkopia < 11:
        print('Komputer wyciągną: ', losowakomputer)
    if grakomputer == 1:
        sumakomputer = sumakomputer + losowakomputer

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

    print('\nSuma twoich liczb wynosi: ', suma)
    print('Suma liczb komputera wynosi: ', sumakomputer)

    if dobieranie == 1:
        wybor = (input('\nDobierz (napisz cokolwiek) albo stop (stop): '))
    if wybor == 'stop':
        dobieranie = 0

    # Sztuczna inteligencja:
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
    print('\nWyrzuciłeś oczko perskie!')
    print('Suma liczb komputera wynosi: ', sumakomputer)
elif a2 == 2:
    print('\nSuma twoich liczb wynosi: ', suma)
    print('Komputer wyrzucił oczko perskie!')
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
