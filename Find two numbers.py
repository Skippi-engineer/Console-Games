#
# Simple console game find a pair of numbers:
#

from random import randint


index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
ar = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]

for i in range(0, 4):
    for j in range(0, 15):
        r = randint(0, 15)
        ar[r], ar[j] = ar[j], ar[r]


game = True
pairs = 0
rounds = 0
while game:
    print("\nIndexes available:", index)
    a = int(input("\nEnter index a: "))
    print("The value for the index", a, "is:", ar[a])
    b = int(input("\nEnter index b: "))
    print("The value for the index", b, "is:", ar[b])
    print("\n------------")

    if ar[a] != 0 and ar[b] != 0:
        rounds += 1
        if ar[a] != ar[b]:
            print("\nYou couldn't find a pair of numbers! t[" + str(a) + "] =", ar[a], ", t[" + str(b) + "] =", ar[b])
    else:
        print("\nYou must give two indexes that have not been discovered!")

    if ar[a] == ar[b] and ar[a] != 0 and ar[b] != 0:
        print("\nYou found a pair of numbers! t[" + str(a) + "] =", ar[a], ", t[" + str(b) + "] =", ar[b])

        ar[a] = 0
        ar[b] = 0
        index.remove(a)
        index.remove(b)
        pairs += 1

    if len(index) == 0:
        game = False

print("\n------------\nCongratulations! You discovered all the pairs!")
print("It took", rounds, "rounds!")
