def find(lista,liczba):
    lita2=[]
    index = 0
    for w in lista:
        if liczba == w:
            lista2.append(index)
        index+=1
    return lista2


L1 = find([3,5,1,5,7],5)
print(L1)
