from fn import wyswietl_biblioteki, wyswietl_ksiazki, dodaj_biblioteke, dodaj_ksiazke, usun_ksiazke, edytuj_strony
import time
biblioteki = []

while True:
    print("\nWybierz operację:")
    print("1. Wyświetl biblioteki")
    print("2. Dodaj bibliotekę")
    print("3. Wybierz bibliotekę")
    print("4. Wyjdź")

    wybor = input("Twój wybór: ")

    if wybor == "1":
        wyswietl_biblioteki(biblioteki)
    elif wybor == "2":
        nazwa = input("Podaj nazwę nowej biblioteki: ")
        dodaj_biblioteke(biblioteki, nazwa)
    elif wybor == "3":
        if not biblioteki:
            print("Nie ma dostępnych bibliotek. Dodaj nową.")
            time.sleep(1)
            continue

        wyswietl_biblioteki(biblioteki)
        indeks_biblioteki = int(input("Wybierz numer biblioteki: ")) - 1

        while True:
            biblioteka = biblioteki[indeks_biblioteki]
            print(f"\nObecnie wybrana biblioteka: {biblioteka['nazwa']}")
            print("a - Wyświetl książki")
            print("b - Dodaj książkę")
            print("c - Usuń książkę")
            print("d - Edytuj liczbę stron")
            print("e - Powrót do menu głównego")

            wybor_biblioteki = input("Twój wybór: ")

            if wybor_biblioteki == "a":
                wyswietl_ksiazki(biblioteka)
            elif wybor_biblioteki == "b":
                tytul = input("Podaj tytuł książki: ")
                strony = int(input("Podaj liczbę stron: "))
                dodaj_ksiazke(biblioteka, tytul, strony)
            elif wybor_biblioteki == "c":
                id_ksiazki = input("Podaj ID książki do usunięcia: ")
                usun_ksiazke(biblioteka, id_ksiazki)
            elif wybor_biblioteki == "d":
                id_ksiazki = input("Podaj ID książki do edycji: ")
                nowe_strony = int(input("Podaj nową liczbę stron: "))
                edytuj_strony(biblioteka, id_ksiazki, nowe_strony)
            elif wybor_biblioteki == "e":
                break
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")
    elif wybor == "4":
        print("Wyjście z programu.")
        time.sleep(1)
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        time.sleep(1)
