imiona = ["Arkadiusz", "Wiola", "Antek"]


while True:
    try:
        imie = str(input("Podaj imie:"))
        if imie in imiona:
            print("masz dostep")
            continue
        elif(imie == "k"):
            break
        elif imie not in imiona:
            print("brak")
            continue
        
    except ValueError:
        print("Bledne dane")