# Zadanie 5 (5.py) Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik). Wprowadzamy
# liczbę punktów dla każdego studenta. Napisz program, który obliczy średnią liczbę punktów w grupie z
# wykorzystaniem pętli while




n = int(input("Podaj n"))
a = 1
suma = 0

while a<=n:
    b=int(input(f"Podaj liczbę punktów studenta {a} :"))
    suma+=b
    a+=1

else: print(suma/n)
