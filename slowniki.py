slownik = []

while True:
    try:
        wybor = int(input("\n ------------------- \n Co chcesz zrobić: \n 1. Dodaj \n 2. Szukaj \n 3. Pokaz wszystkie \n 4. Usuń słowo \n 5. Zakończ program: " ))
        if(wybor==1):
            wyraz = str(input("Dodaj slowo do slownika: "))
            slownik.append(wyraz.lower().capitalize())
            continue
        if(wybor==2):
            szukaj = input("Wprowadz szukane słowo: ").lower().capitalize()
            if szukaj in slownik:
                print(f"Jest slowo {szukaj}")
            else:
                print(f"Nie ma słowa {szukaj}")
        if(wybor==3):
            print("Słowa w słowniku: \n")
            for x in slownik:
                print(x)
            continue
        if(wybor==4):
            slowo = input("Które słowo chcesz usunąć?: ").lower().capitalize()
            if slowo in slownik:
                slownik.remove(slowo)
                print(f"Slowo {slowo} zostało usunięte ze słownika")
            else:
                print(f"Nie ma słowa {slowo} w slowniku")
        if(wybor==5):
            print("Koniec programu")
            break
    except ValueError:
        print("Coś poszło nie tak")