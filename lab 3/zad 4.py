# Zadanie 4 (4.py) Zmodyfikuj program z zad. 1 tak, aby przechodząc po kolejnych liczbach przedziału, wypisywać
# tylko liczby parzyste, a nieparzyste – pomijać. Użyj instrukcji continue.

a = int(input("podaj liczbę a: "))
b = int(input("podaj liczbę b: "))

if b<a:
    a,b=b,a

while b>=a:
    if a%2 == 1:
        a = a + 1
        continue
    print(a, end=' ')
    a=a+1