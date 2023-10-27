def argoritmo_burbuja(lista):
    numero= len(lista)
    listafinal=lista
    for i in range (numero-1):
        for j in range(numero-1-i):
            if lista[j] > lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return listafinal

if __name__=="__main__":
    lista=[5, 3, 1, 2, 4]
    listafinal=argoritmo_burbuja(lista)
    print(listafinal)
