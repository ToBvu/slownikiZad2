import time
import uuid

def wyswietl_biblioteki(biblioteki):
    print("Lista bibliotek:")
    for idx, biblioteka in enumerate(biblioteki, start=1):
        print(f"{idx}. {biblioteka['nazwa']}")

def wyswietl_ksiazki(biblioteka):
    print(f"\nLista książek w bibliotece {biblioteka['nazwa']}:")
    for id_ksiazki, info_ksiazki in biblioteka['ksiazki'].items():
        print(f"{id_ksiazki}: {info_ksiazki['tytul']} - {info_ksiazki['strony']} stron, Dodano: {info_ksiazki['czas_utworzenia']}")

def dodaj_biblioteke(biblioteki, nazwa):
    biblioteka = {'nazwa': nazwa, 'ksiazki': {}}
    biblioteki.append(biblioteka)
    print(f"Dodano bibliotekę: {nazwa}")
    time.sleep(1)

def dodaj_ksiazke(biblioteka, tytul, strony):
    id_ksiazki = str(uuid.uuid4())
    czas_teraz = time.strftime("%Y-%m-%d %H:%M:%S")
    biblioteka['ksiazki'][id_ksiazki] = {'tytul': tytul, 'strony': strony, 'czas_utworzenia': czas_teraz}
    print(f"Dodano książkę '{tytul}' do biblioteki {biblioteka['nazwa']}")
    time.sleep(1)

def usun_ksiazke(biblioteka, id_ksiazki):
    if id_ksiazki in biblioteka['ksiazki']:
        del biblioteka['ksiazki'][id_ksiazki]
        print(f"Usunięto książkę o ID {id_ksiazki} z biblioteki {biblioteka['nazwa']}")
        time.sleep(1)
    else:
        print(f"Książka o ID {id_ksiazki} nie istnieje w bibliotece {biblioteka['nazwa']}")
        time.sleep(1)

def edytuj_strony(biblioteka, id_ksiazki, nowe_strony):
    if id_ksiazki in biblioteka['ksiazki']:
        biblioteka['ksiazki'][id_ksiazki]['strony'] = nowe_strony
        print(f"Zaktualizowano liczbę stron dla książki o ID {id_ksiazki} w bibliotece {biblioteka['nazwa']}")
        time.sleep(1)
    else:
        print(f"Książka o ID {id_ksiazki} nie istnieje w bibliotece {biblioteka['nazwa']}")
        time.sleep(1)
