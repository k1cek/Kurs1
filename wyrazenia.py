# wyrazenia list

liczby = [1,2,3,4,5,6,7,8,9]

# list comprehension - zamiast pisać długą pętlę, "ogarniasz" całą operację w jednej linijce. list komprihenszyn
potegi_dwojki = [i**2 for i in liczby]
liczby_parzyste = [i for i in potegi_dwojki if(i%2==0)]
generator_potegi2 = [i**2 for i in range(20)]

# print(potegi_dwojki)
# print(liczby_parzyste)
# print(generator_potegi2)


# wyrazenia słownikowe

names = {"Monia", "Basia", "Grzesiek", "Karol"}
liczby2 = {1,2,3,4,5,6,7,8,9}
wyswietl = {name : len(name) for name in names}

# print(wyswietl)

multipliedNum = {
    num : num*num # KLUCZ : WARTOSC
    for num in liczby2
}

# print(multipliedNum)


def czy_parzysta(list_comprehension):
    if any(i % 2 == 0 for i in list_comprehension):  # Użycie any() zamiast list comprehension
        return "Sa"
    return "nie ma"

numbers1 = [1, 3, 5, 7, 10]
print(czy_parzysta(numbers1))  # ✅ Wynik: "nie ma"


 
#przekazanie kilku list jako argument

def czy_parzysta2(*lists):  # Przyjmuje dowolną liczbę list
    if any(i % 2 == 0 for lista in lists for i in lista):  # Sprawdza każdą listę
        return "Sa"
    return "nie ma"

numbers3 = [1, 3, 5, 7, 11]
numbers4 = [3, 1, 5, 1, 11]

print(czy_parzysta2(numbers3, numbers4)) 