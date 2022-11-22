# Zadanie 2.
# • Wypisz wszystkie pary klucz:wartość występujące w słowniku:
# sample_dict = {
#  "name": "Kelly",
#  "surname": "Jones",
#  "age": 25,
#  "salary": 8000,
#  "city": "New york"}
# • Utwórz słownik, wybierając ze słownika sample_dict pary o kluczach zapisanych w liście.
# Wskazówki:
# − przejdź za pomocą pętli po kluczach zapisanych w liście;
# − następnie sprawdź, czy dany klucz występuje w słowniku; jeśli występuje, dodaj go (parę
# klucz:wartość) do nowego słownika.
# • Usuń ze słownika wartości, których klucze występują w liście.
# • Sprawdź, czy wartość „Jones” występuje w słowniku.
# • Zmień w słowniku klucz ‘city’ na ‘location’.

sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

# for key in sample_dict:
#     print(f'{key:<10}={sample_dict[key]:>10}')

for k,v in sample_dict.items():
    print(f'{k:<10}={v:>10}')

L=['age','name']
D={}
i = 0
while i<len(L):
    if L[i] in sample_dict.keys():
        D[L[i]]=sample_dict[L[i]]

    i+=1
print(D)


# sample_dict = { "name": "Kelly", "surname": "Jones", "age": 25, "salary": 8000, "city": "New york"}
# for key in sample_dict:
#  print(f"{key:<10}={sample_dict[key]:>10}")


#  for k in L:
#  if k in sample_dict.keys():
#  D[k]=sample_dict[k]
L = ['age', 'name']
D={}
D = {k:sample_dict[k] for k in L if k in sample_dict.keys()}
print(D)


for k in L:
     del sample_dict[k]
print(sample_dict)

if "Jones" in sample_dict.values():
    print("Wartość Jones występuje")
else:
    print("Nie wsytępuje")