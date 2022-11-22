# Zadaie 1.
# • Utwórz listę values zawierającą liczby 10, 20, 30. Utwórz drugą listę keys zawierającą nazwy tych liczb w
# języku angielskim (lub polskim). Dokonaj konwersji tych list w słownik.
# Wskazówki:
# − użyj funkcji zip(), która pobiera dwie sekwencje (takie jak list, dict, str), łączy je w krotki (pary) i
# zwraca;
# − lub wykonaj iterację listy za pomocą pętli for i funkcji range(). W każdej iteracji dodaj nową parę kluczwartość do słownika.
# • Utwórz drugi słownik metodą słów kluczowych ( dict(klucz1=wartość1, klucz2=wartość2)), gdzie kluczem
# będą nazwy liczb 30, 40, 50, a wartościami – liczby 30, 40, 50.
# • Połącz dwa słowniki w jeden nowy słownik.n

#
# values = [10,20,30]
# keys = ["dziesięć", "dwadzieścia", "trzydzieści"]
# print(list(zip(keys,values)))
#
# D=dict(zip(keys,values))
# print(D)

values = [10,20,33]
keys = ["dziesięć", "dwadzieścia", "trzydzieści"]
D={}
for i in range (len(values)):
    D[keys[i]]=values[i]

print(D)

A=dict(trzydzieści=30, czterdzieści=40, pięćdziesiąt=50)
print(A)

# D.update(A)
D3=D.copy()
D3.update(A)
print(D3)
print(D)
print(A)
