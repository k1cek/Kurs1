import time

def imiona(imie, nazwisko, adres="Poznan"):
    return(imie, nazwisko, adres)

# print(imiona(adres="Leszek", imie="Zajac", nazwisko="Luban"))


def function_performance(func, arg, how_many_times = 1):
    sum = 0

    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end-start)
    return sum


setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]

def check(cont):
    if cont in setContainer:
        return ("Tak")
    else:
        return ("Nie")
    

# print(function_performance(check, 200, how_many_times=2000000))



def count(*liczby):
    return sum(liczby)


# print(count(2,4,1,2,4,5,10,-10))

# Funkcja any() sprawdzająca czy przesłana lista zawiera liczby parzyste

def any(liczba):
    liczby_parzyste = [i for i in liczba if(i%2==0)]
    if liczby_parzyste:
        return("sa")
    else:
        return("nie")

numbers1 = [1,3,5,7]
print(any(numbers1))


# uzycie z any

def czy_parzysta(list_comprehension):
    if any(i % 2 == 0 for i in list_comprehension):  # Użycie any() zamiast list comprehension
        return "Sa"
    return "nie ma"

# numbers5 = [1, 3, 5, 7]
print(czy_parzysta(numbers1))  # ✅ Wynik: "nie ma"
