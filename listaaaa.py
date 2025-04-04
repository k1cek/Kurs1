# items = [1, 5, 8, 12, 3, 7]
# Twoje rozwiązanie tutaj

# filtered = [i for i in items if i>5]

# print(filtered)


# wiek = int(input(f"Podaj wiek: "))
# print(f"Masz lat {wiek}")


# liczba = int(input(f"Podaj liczbę: "))
# if liczba%2==0:
#     print(f"{liczba} jest liczbą parzystą")
# else:
#     print(f"{liczba} jest liczbą nieparzystą")


# low = 1
# high = 100
# proby = 0

# print("Pomyśl o liczbie od 1 do 100, a ja ją zgadnę! 😎")
# input("Gdy będziesz gotowy, naciśnij Enter...")

# while True:
#     strzal = (low + high) // 2
#     proby += 1
#     print(f"Zgaduję: {strzal}")

#     odpowiedz = input("Za dużo (wpisz 'więcej'), za mało (wpisz 'mniej'), czy zgadłem (wpisz 'tak')? ").lower()

#     if odpowiedz == "tak":
#         print(f"Ha! Zgadłem za {proby} razem! 🎉")
#         break
#     elif odpowiedz == "więcej":
#         low = strzal + 1
#     elif odpowiedz == "mniej":
#         high = strzal - 1
#     else:
#         print("Nie rozumiem odpowiedzi. Wpisz: więcej / mniej / tak")



# wyraz = str(input("Podaj zdanie: ")).lower()
# liczba = 0
# for i in wyraz:
#     if i in "aeiouy":
#         liczba += 1
# print(f"Podane zdanie ma {liczba} samogłosek")


#Parzyste i >5: [6, 10, 12, 14, 8]  
#Inne: [3, 2, 7, 4, 9, 1, 5]  


# liczby = [3, 6, 2, 7, 4, 9, 10, 1, 12, 14, 5, 8]

# parzyste = [i for i in liczby if i>5 and i%2==0]
# nieparzyste = [i for i in liczby if i<5 and i%2!=0]

# print(f"Liczby parzyste i większe od 5 to: {parzyste}. Lista zawiera {len(parzyste)} liczb")
# print(f"Liczby nieparzyste i mniejsze od 5 to: {nieparzyste}. Lista zawiera {len(nieparzyste)} liczb")


#--------
# imiona = ["Ala", "Bartek", "Ola", "Tomek", "Zosia"]

# upper_names = [i.upper() for i in imiona if len(i)>3]

# print(upper_names)



#--------
# liczby = [1, 4, 7, 10, 15, 22, 30]

# lista_nowa = [i**2 for i in liczby if i%5==0]

# print(lista_nowa)


#--------------

# slowa = ["kot", "pies", "hipopotam", "lew", "koń", "słoń"]

# zwierzeta_dlugie = [i[::-1] for i in slowa if len(i)>3]

# print(zwierzeta_dlugie)


#-----------------

# macierz = [[1, 2], [3, 4], [5, 6]]
# lista = [i for j in macierz for i in j]
# print(lista)


#-----------------

# macierz = [[1, 2, 3], [4, 5], [6, 7, 8]]

# lista = [element*10 for podlista in macierz for element in podlista if element%2==0]

# print(lista)


#--------------------

# zwierzaki = [["kot", "koń", "pies"], ["pantera", "pingwin", "papuga"], ["lew", "lama", "lis"]]

# zwierzaki_2 = [element.upper() for podlista in zwierzaki for element in podlista if element.startswith("p")]

# print(zwierzaki_2)

#--------------------

# imiona = [["Anna", "Bartek", "Ala"], ["Ania", "Tomek"], ["Agata", "Ola", "Antoni"]]

# imiona_2 = [element.lower() for podlista in imiona for element in podlista if element.startswith("A")]

# print(imiona_2)

#--------------------
# Twoje zadanie:

# Spłaszcz listę (czyli przetwórz każdą liczbę ze wszystkich podlist)
# Dla każdej liczby:
# jeśli jest ujemna, zapisz jako string "ujemna"
# jeśli jest parzysta, podnieś ją do potęgi 2
# jeśli jest nieparzysta, dodaj do niej 10
# Stwórz nową listę zawierającą te przekształcone wartości
# Wypisz wynik

# liczby = [[-3, 2, 5], [0, -1, 4], [-6, 8, 9]]

# wynik = ["ujemna" if element<0 else (element*2 if element%2==0 else element+10) 
#          for podlista in liczby 
#          for element in podlista]

# print(wynik)


#-------------------

# imiona = [["Anna", "Bartek"], ["Ola", "Andrzej"], ["Iza", "Ada"]]

# imiona_a = ["A_"+element if element.startswith("A") else element for podlista in imiona for element in podlista]

# print(imiona_a)


#------------------


# pary = [["a", 1], ["b", 2], ["c", 3]]

# slownik = {klucz:wartosc for klucz, wartosc in pary}

# print(slownik)


#-------------------

# liczby = [1, 2, 3, 4, 5]

# slownik = {klucz:klucz**2 for klucz in liczby}

# print(slownik)

#-------------------

# slowa = ["dom", "drzewo", "okno", "piesek"]

# slownik = {klucz:len(klucz) for klucz in slowa if len(klucz)>4}

# print(slownik)


#-------------------

# dane = [["Anna", 25], ["Bartek", 30], ["Celina", 28], ["Dawid", 31]]

# slownik = {klucz[0]:wartosc for klucz, wartosc in dane}

# print(slownik)

#-------------------

# slowa = ["kot", "pies", "hipopotam", "lew"]

# slownik = {klucz:[litera.upper() for litera in klucz] for klucz in slowa}

# print(slownik)


# odpowiedzi = [" tak", "Nie ", "  TAK ", "nie", "   tAk"]


# lista = [i.strip().lower() for i in odpowiedzi]

# print(lista)


#-----------------

def sprawdz_logowanie(uzytkownik, haslo):
        if not isinstance(uzytkownik, str) or not isinstance(haslo, str):
             return "Nieprawidłowy typ danych"
        elif uzytkownik=="admin" and haslo=="tajne123":
            return "Zalogowano"
        else:
            return "Błędne dane logowania"

        

assert sprawdz_logowanie("admin", "tajne123") == "Zalogowano"
assert sprawdz_logowanie("admin", "haslo") == "Błędne dane logowania"
assert sprawdz_logowanie(123, "tajne123") == "Nieprawidłowy typ danych"
assert sprawdz_logowanie("admin", 456) == "Nieprawidłowy typ danych"



