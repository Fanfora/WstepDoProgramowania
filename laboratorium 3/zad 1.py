# Zadanie 1 (1.py) Napisz skrypt, który pobierze od użytkownika dwie liczby całkowite. Następnie zaczynając od
# mniejszej liczby, wypisze kolejne liczby aż do osiągnięcia wartości drugiej (większej) liczby.
# Np. Wejście: 10, 5
# # Wyjście: 5, 6, 7, 8, 9,

a = int(input("podaj liczbę a"))
b = int(input("podaj liczbę b"))

if b<a:
    (a, b) = (b, a)

while b>=a:
    print(a,end=' ')
    a=a+1