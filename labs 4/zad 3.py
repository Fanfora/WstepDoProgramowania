# Zadanie 3. Utwórz pustą listę zwierzeta. Następnie
# • Dodaj kilka nazw zwierząt do listy
# • Posortuj listę
# • Wyświetl pierwszy oraz trzy ostatnie elementy na liście
# • Wyświetl informację o liczbie zwierząt na liście

zwierzeta = []
nazwy = input("Podaj nazwy")
zwierzeta = nazwy.split(" ")

print(zwierzeta[0], zwierzeta[-3:])
print(sorted(zwierzeta))







