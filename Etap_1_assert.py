def podziel(a, b):
        try:
            if not isinstance(a, int) or not isinstance(b, int):
                return "Błąd: nieprawidłny typ danych"
            else:
                return a/b
        except ZeroDivisionError:
            return "Błąd: nie można dzielić przez zero"

assert podziel(10, 2) == 5
assert podziel(5, 0) == "Błąd: nie można dzielić przez zero"
assert podziel("10", 2) == "Błąd: nieprawidłny typ danych"
assert podziel(10, "dwa") == "Błąd: nieprawidłny typ danych"



# def wczytaj_dane(nazwa_pliku):
#     try:
#         with open(nazwa_pliku, "r", encoding="utf-8") as plik:
#             return plik.read()
#     except FileNotFoundError:
#         return "Błąd: plik nie istnieje"
#     except IOError:
#         return "Błąd: nie można odczytać pliku"

# print(wczytaj_dane("test.txt"))             # jeśli plik istnieje
# print(wczytaj_dane("brak.txt"))             # jeśli nie istnieje





# def policz_slowa(tekst):
#     slownik = {}
#     slowa = tekst.split()  # dzieli tekst na listę słów

#     for slowo in slowa:
#         if slowo in slownik:
#             slownik[slowo] += 1
#         else:
#             slownik[slowo] = 1
#     return slownik

#-------------------

#Zlicz wystąpienia słów w tekście


# def policz_slowa(tekst):
#     slownik = {}
#     for slowo in tekst.split():
#         slownik[slowo] = slownik.get(slowo, 0) + 1
#     return slownik




# tekst = "kot pies kot kot pies kura kura"
# print(policz_slowa(tekst))

#wynik
# {'kot': 3, 'pies': 2, 'kura': 1}


# def sprawdz_liczby(lista):
#     nowa = []
#     for element in lista:
#         if isinstance(element, int):
#             nowa.append(element)
#         elif isinstance(element, str):
#             try:
#                 nowa.append(int(element))
#             except ValueError:
#                 pass # ignorowanie jesli sie nic nie da zrobic

#     return nowa


# wejscie = ["5", "abc", 3, None, "8", "2a", 4]
# print(sprawdz_liczby(wejscie))


#-------------------


def zweryfikuj_dane(lista):
    nowa_lista = []

    for wyraz in lista:
                if isinstance(wyraz, int):
                    nowa_lista.append(wyraz)
                elif isinstance(wyraz, str):
                    if wyraz.strip() == "":
                         continue
                    try:
                        nowa_lista.append(int(wyraz))
                    except ValueError:
                        nowa_lista.append(f"tekst:{wyraz}")

        
    return nowa_lista


# wejscie = ["123", 456, "abc", "789", None, "", True]
# print(zweryfikuj_dane(wejscie))




#------------------
#zwiekszenie wartosci o 5 - slownik 
def zwiekszenie(suma):
    slownik = {}
    for klucz, wartosc in suma.items():
          slownik[klucz] = wartosc+5
    return slownik
          

# oceny = {"Bartek": 3, "Ania": 4, "Kasia": 5}
# print(zwiekszenie(oceny))





#-------------------
# znajdz osobe z ocena 5 i wypisz tylko imie osoby

def ocena_5_comp(ocena):
     return [{k:v for k, v in ocena.items() if v==5}]

def ocena_5(ocena):
    oceny = []
    for klucz, wartosc in ocena.items():
          if wartosc == 5:
               oceny.append(klucz)
    return oceny

# oceny = {"Bartek": 3, "Ania": 5, "Kasia": 5, "Tomek": 4}
# print(ocena_5(oceny))
# print(ocena_5_comp(oceny))




#-------------------
#liczenie liter w imionach

def liczenie(ilosc):
    imiona = {}

    for klucz in ilosc:
         imiona[klucz] = len(klucz)
    return imiona


# imiona = ["Ala", "Bartek", "Tomek"]
# print(liczenie(imiona))



#------------
# lista z kluczy o wartosci wiekszej niz 10


def more_10(liczba):
     return [k for k, v in liczba.items() if v>10]

# dane = {"Ala": 8, "Bartek": 12, "Kasia": 15, "Tomek": 9}
# print(more_10(dane))


#-----------------
#nowy slownik z długosci imion

# 1. klasyk
def dlugosc(wartosc):
    lista = {}
    for element in wartosc:
         lista[element] = len(element)
    return lista

# 2. list comprehension

def dlugosc_2(liczba):
     return {element: len(element) for element in liczba}
# imiona = ["Ewelina", "Łukasz", "Ada", "Tomek"]
# print(dlugosc(imiona))
# print(dlugosc_2(imiona))



#--------------------
# zwieksz wartosc o 2 - nowy slownik
# 1. klasyk
def wartosc_plus2(liczba):
    lista = {}
    for klucz, wartosc in liczba.items():
         lista[klucz] = wartosc + 2
    return lista

# 2. list comprehension
def wartosc_plus2_v2(liczba):
     return {k.upper():v*2 for k, v in liczba.items()}

# punkty = {"Ala": 10, "Bartek": 8, "Kasia": 7}
# print(wartosc_plus2(punkty))
# print(wartosc_plus2_v2(punkty))


#------------------------
#Policz, ile razy każda litera występuje w słowie

# wynik: {'l': 1, 'a': 1, 'k': 1, 'i': 1, 'e': 1, 'r': 1}

# 1. comprehension
# Więc jeśli chcesz kod bardziej wydajny i elegancki, używaj set() 😎

def liczyny_comp(slowo):
    return {element: slowo.count(element) for element in set(slowo)} # set jest wydajniejsze bo nie liczy dla kazdej litery
    # return {element: slowo.count(element) for element in slowo} # tu liczy dla kazdej 

# 2. klasyk
def liczymy(slowo):
    ilosc = {}
    for litera in slowo:
        if litera in ilosc:
              ilosc[litera] +=1
        else:
             ilosc[litera] = 1
    return ilosc
         

# slowo = "banan"
# print(liczymy(slowo))
# print(liczyny_comp(slowo))


#-----------------------------------

# ZADANIE U5 – Wyświetl pary imię + ocena tylko jeśli ocena to 5

# 1. Klasyk

def pary(dane):
    wynik = {}
    for klucz, wartosc in dane.items():
        if wartosc ==5:
            wynik[klucz] = wartosc
    return wynik

# 2. dict comprehension

def pary_comp(dane):
     return {klucz:wartosc for klucz, wartosc in dane.items() if wartosc==5}

# oceny = {"Ala": 5, "Bartek": 4, "Kasia": 5, "Tomek": 3}
# print(pary(oceny))
# print(pary_comp(oceny))



#------------------------


def czy_parzysta(liczba):
     return liczba%2==0

# assert czy_parzysta(2) == True
# assert czy_parzysta(3) == False
# assert czy_parzysta(0) == True




#------------------ ZADANIE 1 – Zwróć słownik z danych w pliku
# oczekiwany wynik: {"Tomek": 28, "Ania": 31, "Bartek": 25, "Kasia": 29}


def czytaj_dane(nazwa_pliku):
    slownik = {}
    with open(nazwa_pliku, "r", encoding="utf-8") as plik:
        for klucz, wartosc in plik.items():
            slownik[klucz] = wartosc.strip().split(";")
            # print(f"{imie} ma {wiek} lat.")
        return slownik

czytaj_dane("dane.txt")


#----------------------------