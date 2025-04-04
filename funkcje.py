import time

#slownik na funkcjach

def zabawa(dane):
    for i in dane:
        print(f"Imię: {i['imie']}")
        print(f"Nazwisko: {i['nazwisko']}")


lista = [
    {"imie": "Lukasz", "nazwisko": "zajac", "wiek": 33, "adres": "poznan"}
]


# kicua = zabawa(lista)

# print(kicua)



#--------------- drugi programik
# napisz program, który policzy sumę liczb od 1 do podanej liczby

# 1. pętla

def sumuj_petla(liczba):
    suma = 0
    for liczba in range(1, liczba+1):
        suma = suma + liczba
    return suma

start1 = time.perf_counter()
print(sumuj_petla(20))
end1 = time.perf_counter()

# 2. Generator / Lista wyrazeniowa - ulubiona ;) - nawiasy kwadratowe

def sum_generator(liczba):
    return sum((liczba for liczba in range(1, liczba+1)))

start2 = time.perf_counter()
print(sum_generator(20))
end2 = time.perf_counter()

                                            # tworzy liste w pamieci?
# [liczba for liczba in range(1, liczba+1)]	✅ Tak	    ❌ Wolniejsze, więcej pamięci
# (liczba for liczba in range(1, liczba+1)) ❌ Nie       ✅ Szybsze, oszczędza pamięć




# 3. metoda na wzór na ciąg arytmrtyczny

def wzor(liczba):
    return (1+liczba) / 2*liczba

start3 = time.perf_counter()
print(wzor(20))
end3 = time.perf_counter()


print(end1-start1)
print(end2-start2)
print(end3-start3)


