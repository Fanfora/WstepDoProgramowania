# Zadanie 3 (3.py) Napisz skrypt działający jak prosty kalkulator, który potrafi dodawać, odejmować, mnożyć,
# dzielić oraz obliczać potęgę.
# Przykład: Jaką operację chcesz wykonać?
# 1) dodawanie
# 2) odejmowanie
# 3) mnożenie
# 4) dzielenie
# 5) potęgowanie
# Wpisz numer operacji: 2
# Podaj argument 1: 34
# Podaj argument 2: 5
# Wynik: 29

print('''1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie
''')
x = int(input('jaką akcje chcesz wykonać?'))
a=int(input('podaj a:'))
b=int(input('podaj b:'))
if x == 1:
    print(a + b)

elif x == 2:
    print(a - b)

elif x == 3:
    print(a * b)

elif x == 4:
    print(a / b)

elif x == 5:
    print(a ** b)

else:
    print('liczba nieprawidlowo wprowadzona')


x = int(input( """Jaką operację chcesz wykonać? 1) dodawanie 2) odejmowanie 3) mnożenie 4) dzielenie 5) potęgowanie""")) y = int(input("podaj 1 liczbe")) z = int(input("podaj 2 liczbe")) if x == 1: print("twój wynik to", y+z ) elif x == 2: print("twój wynik to", y-z ) elif x == 3: print("twój wynik to", y*z ) elif x == 4: if z == 0: print("nie dziel przez 0") exit() print("twój wynik", y/z) elif x == 5: print("twój wynik to", y**z ) else: print("zły wybór")
