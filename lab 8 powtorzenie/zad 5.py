# Zadanie 5. Napisz program działający jak prosty kalkulator. W tym celu utwórz funkcje dodawanie(),
# odejmowanie(), mnożenie() oraz dzielenie(). Następnie utwórz słownik, którego kluczem jest działanie, a
# wartością – nazwa odpowiedniej funkcji.
# Uwaga: funkcja jest obiektem, a nazwa funkcji – nazwą (referencją) tego obiektu.


def dodawanie(a, b):
    return a+b
def odejmowanie(a,b):
    return a-b
def mnożenie(a,b):
    return a*b
def dzielenie(a,b):
    if b!=0:
        return a/b



a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
x = input()


słownik = {'+':dodawanie,'-':odejmowanie,'*':mnożenie,'/':dzielenie}
print(słownik[x](a,b))