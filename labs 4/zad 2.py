# Zadanie 2.
# • Utwórz listę zestaw_1 zawierającą liczby losowe z przedziału [1, 10]. Liczbę elementów listy podaje
# użytkownik. Wyświetl listę.
# • Utwórz drugą listę zestaw_2 zawierającą liczby losowe z przedziału [5, 15]. Liczbę elementów listy
# podaje użytkownik. Wyświetl listę.
# • Pobierz od użytkownika liczbę. Napisz instrukcję warunkową, która na podstawie wartości
# zapisanych w listach wyświetli jeden z poniższych komunikatów: „Liczba z zestawu 1”, „Liczba z
# zestawu 2” albo „Nie ma takiej liczby w obu zestawach”.
# • Utwórz listę zestaw_1_2 będącą złączeniem wartości z list zestaw_1 oraz zestaw_2. Posortuj i wyświetl
# listę


import random

zestaw_1 = []

x = int(input("Podaj liczbę"))

for i in range(x):
    y = random.randint(1,10)
    zestaw_1.append(y)
print(zestaw_1)


k = int(input("Podaj liczbę wartości znajdujących się w liście 2"))
zestaw_2 = [random.randint(5,15) for y in range(k)]
print(zestaw_2)

l = int(input("podaj liczbę"))

if l in zestaw_1:
    print("Liczba z zestawu 1")
elif l in zestaw_2:
    print("Liczba z zestawu 2")
else:
    print("Nie ma takiej liczby w obu zestawach")

zestaw_1_2 = zestaw_1 + zestaw_2
print(zestaw_1_2)
zestaw_1_2.sort()
print(zestaw_1_2)
