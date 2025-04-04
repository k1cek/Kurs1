# Losowanie liczby - pętla while z TRY

import random
wylosowana_liczba = random.randint(1, 100)
wynik = 0

print("Pomyślałem sobie liczbę od 1 do 100")

while True:
    try:
        wynik+=1
        # print(wylosowana_liczba)
        liczba = int(input("Podaj liczbę: "))
        if(liczba<=0 or liczba>100):
            print("Podaj liczbę z zakresu od 1 do 100")
        elif(liczba<wylosowana_liczba):
            print("To za mało")
        elif(liczba>wylosowana_liczba):
            print("To za duzo")
        elif(liczba==wylosowana_liczba and wynik==1):
            print(f"WOOOOW! Niesamowite! Zgadłeś za 1 razem! Ta liczba to {wylosowana_liczba}")
            break
        elif(liczba==wylosowana_liczba):
            print(f"BRAWO! Zgadłeś za {wynik} razem! Ta liczba to {wylosowana_liczba}")
            break
    except ValueError:
        print("Podaj poprawną liczbę:")
        

