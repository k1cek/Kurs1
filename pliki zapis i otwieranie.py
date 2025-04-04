#pliki zapis i otwieranie

lista = [1,2,3,4,5,6,7]


def spradz(liczba):
    for i in liczba:
        print(i)
    if 5 in liczba:
        print("znaleziono 5")


print(spradz(lista))