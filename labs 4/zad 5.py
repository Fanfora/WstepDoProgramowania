# Zadanie 5. Utwórz listę punkty będącą listą punktów zdobytych z pewnego egzaminu przez grupę 15 studentów.
# Punkty niech będą liczbami rzeczywistymi z przedziału [0; 50]. Następnie
# • Wyświetl informację o największej i najmniejszej ilości zdobytych punktów
# • Wyświetl indeks pierwszego wystąpienia punktów podanych przez użytkownika. Jeżeli taka liczba
# punktów nie występuje na liście, wyświetl odpowiedni komunikat
# • Oblicz średnią punktów liczbę punktów z egzaminu
# • Oblicz, ile osób zdobyło punkty powyżej, a ile poniżej średniej
# • Wyświetl punkty poniżej średniej
# • Wyświetl punkty powyżej średniej


import random
punkty = []
y = 0
while y < 15:
    x = random.uniform(0,50)
    x = round(x,2)
    punkty.append(x)
    y += 1


print(punkty)

print(max(punkty))
print(min(punkty))

k = float(input("podaj punkty"))
if k in punkty:
    print(punkty.index(k))
else:
    print("Wartość nie występuje na liście")


