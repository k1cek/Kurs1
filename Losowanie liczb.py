#Losowanie liczb

import random

lista = [1,2,3,4]

# print(lista)


def losowanie(liczba):
    for i in liczba:
        return i

from collections import Counter
# print(Counter(random.choices(lista, [80, 15, 4, 1], k=10)))

#choice - zwraca losowy element
#choices - zwraca listę elementów i ma wieksze mozliwosci


# LOTTO 6 z 49

def lotto(ilosc_liczb, wszystkie):
    liczby = []
    while(len(liczby)<ilosc_liczb):
        liczba = random.randint(1, wszystkie)
        if liczba not in liczby: #unikalne liczby
            liczby.append(liczba)
    return(liczby)

print(lotto(6, 149))
