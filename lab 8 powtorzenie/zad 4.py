# Zadanie 4.Napisz funkcję znaki(), która zlicza znaki w string’u za pomocą słownika: znaki stanowią klucze, liczba
# znaków – wartości. Parametrem funkcji jest string. Funkcja ma zwracać słownik z wynikami. Wypisz słownik
# uporządkowany według kluczy.
# Wskazówka: użyj metody get(), która przy dostępie do wartości klucza, którego nie ma w słowniku,
# zgłasza wyjątek KeyError. Aby uniknąć tego błędu metoda get może zwrócić wartość zdefiniowaną przez
# użytkownika (drugi parametr).
# Np. Wejście: „znaki napisu”
# Wyjście: {'z': 1, 'n': 2, 'a': 2, 'k': 1, 'i': 2, ' ': 1, 'p': 1, 's': 1, 'u': 1}



def znaki(nazwa):
    D = {}
    for v in nazwa:
        if v in D:
            D[v] = D[v] + 1
        else:
            D[v] = 1
    return D


D2 = znaki('napisap')
l = sorted(D2.keys())
for k in l:
    print(k,D2[k])
print(D2)
