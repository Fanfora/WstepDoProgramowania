# Zadanie 2 (2.py) Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała.

litera = input('podaj litere')
if(len(litera)>1):
    print('wprowadzono więcej niż jeden znak')
    exit()
if(len(litera)==0):
    print('nie wprowadzono litery')
    exit()

if (litera > 'a' <= 'z'):
    print('mała litera')
elif('A'<= litera <= "Z"):
    print("Duża litera")
else:
    print("nie jest literą")
