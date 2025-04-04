def sredni_wiek(slownik):
    if not slownik:
        return 0
    return sum(slownik.values()) / len(slownik)


def test_sredni_wiek_typowe_dane():
    dane = {"Ala": 30, "Ola": 32, "Ela": 28}
    assert sredni_wiek(dane) == 30

def test_sredni_wiek_jedna_osoba():
    dane = {"Ania": 40}
    assert sredni_wiek(dane) == 40

def test_sredni_wiek_puste():
    dane = {}
    assert sredni_wiek(dane) == 0
