from Etap_2 import pobierz_uzytkownikow  # zamień "twoj_plik" na nazwę swojego pliku .py

def test_liczba_uzytkownikow():
    uzytkownicy = pobierz_uzytkownikow()
    assert isinstance(uzytkownicy, list)
    assert len(uzytkownicy) == 10

def test_klucze_uzytkownika():
    uzytkownicy = pobierz_uzytkownikow()
    pierwszy = uzytkownicy[0]
    assert "name" in pierwszy
    assert "email" in pierwszy
    assert "address" in pierwszy
    assert "city" in pierwszy["address"]

def test_email_uzytkwnika():
    uzytkownicy = pobierz_uzytkownikow()
    for user in uzytkownicy:
        email = user.get("email", "")
        assert isinstance(email, str), f"Email nie jest stringiem: {email}"
        assert email != "", "Email jest pusty"
        assert "@" in email, f"Brak znaku @ w e-mailu: {email}"

        