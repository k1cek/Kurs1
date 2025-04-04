def dziel(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return "Błąd: nieprawidłny typ danych"
        return a / b
    except ZeroDivisionError:
        return "Błąd: nie można dzielić przez zero"


def test_dziel_prawidlowe():
    assert dziel(10, 2) == 5

def test_dziel_przez_zero():
    assert dziel(5, 0) == "Błąd: nie można dzielić przez zero"

def test_dziel_ujemne():
    assert dziel(-10, 2) == -5

def test_dziel_string():
    assert dziel("tekst", 2) == "Błąd: nieprawidłny typ danych"

def test_dziel_brak_typow():
    assert dziel([1, 2], {"b": 5}) == "Błąd: nieprawidłny typ danych"

def test_dziel_float():
    assert dziel(5.0, 2) == 2.5


def czytaj_dane(nazwa_pliku):
    with open(nazwa_pliku, "r", encoding="utf-8") as plik:
        for linia in plik:
            imie, wiek = linia.strip().split(";")
            print(f"{imie} ma {wiek} lat.")

if __name__ == "__main__":
    czytaj_dane("dane.txt")