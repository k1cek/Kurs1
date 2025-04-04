#------------------ ZADANIE 1 – Zwróć słownik z danych w pliku dane.txt
# oczekiwany wynik: {"Tomek": 28, "Ania": 31, "Bartek": 25, "Kasia": 29}


def zwrotka_danych(dane):
    slownik = {}
    with open(dane, "r", encoding="utf-8") as plik:
        for linia in plik:
            imie, wiek = linia.strip().split(";") # strip - Usuwa białe znaki z początku i końca linii – najczęściej \n (znak nowej linii).
            # split - Dzieli tekst po średniku ;, zwracając listę elementów.
            slownik[imie] = int(wiek)
    return slownik


# print(zwrotka_danych("dane.txt"))


#------------------------------

# srednia wieku

def sredni_wiek(slownik):
    if not slownik:
        return 0
    suma = sum(slownik.values())
    return suma / len(slownik)

# print(sredni_wiek(zwrotka_danych("dane.txt")))

import requests

def pobierz_uzytkownikow():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    print(f"Ilość uzytkowników: {len(response.json())}")
    return response.json()  # Zwraca listę słowników

uzytkownicy = pobierz_uzytkownikow()

for user in uzytkownicy:
    print(f"{user['name']} ({user['email']}) z miasta {user['address']['city']}")
