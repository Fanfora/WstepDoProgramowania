a = int(input("podaj liczbę a: "))
b = int(input("podaj liczbę b: "))
if b<a:
    a,b=b,a
while b>=a:
    print(a,end=' ')
    a=a+1