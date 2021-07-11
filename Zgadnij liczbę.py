# 1. Utworzyć tablicę, wypełnić ją 8 parami wartości:
# [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8], a następnie przetasować.

# 2. Wejść do głównej pętli gry, gdzie poprosić gracza o podanie dwóch indeksów
# tablicy które chce sprawdzić. Wyświetlić graczowi informacje o wartościach
# znajdujących się pod wybranymi indeksami. W przypadku trafienia takich
# samych wartości, zwiększyć licznik znalezionych par, jednocześnie zerując w
# tablicy odkryte pola (żeby nie można było ich ponownie odkryć).

# 3. Gra kończy się w momencie, gdy gracz odkryje wszystkie pola.

from array import*
from random import*

t = array('i', [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8])
indeksy = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

n = 0
m = 0
for n in range(0, 4):
    for m in range(0, 15):
        r = randint(0, 15)
        t[r], t[m] = t[m], t[r]


gra = True
pary = 0
tury = 0
while gra:
    print('\nDostępne indeksy:', indeksy)
    a = int(input('\nPodaj indeks: '))
    print('Wartość dla indeksu', a, 'wynosi:', t[a])
    b = int(input('\nPodaj indeks: '))
    print('Wartość dla indeksu', b, 'wynosi:', t[b])

    print('\n------------')

    if t[a] != 0 and t[b] != 0:
        tury += 1
        if t[a] != t[b]:
            print('\nNie udało Ci się odnaleść pary liczb!', 't[', a, '] =', t[a], ', t[', b, '] =', t[b])
    else:
        print('\nMusisz podać indeksy które nie zostały odkryte!')

    if t[a] == t[b] and t[a] != 0 and t[b] != 0:
        print('\nZnalazłeś parę liczb!', 't[', a, '] =', t[a], ', t[', b, '] =', t[b])

        t[a] = 0
        t[b] = 0
        indeksy.remove(a)
        indeksy.remove(b)
        pary += 1

    if len(indeksy) == 0:
        gra = False

print('\n------------\nBrawo wygrałeś odkryłeś wszystkie pola!')
print('Zajeło to', tury, 'tur.')
