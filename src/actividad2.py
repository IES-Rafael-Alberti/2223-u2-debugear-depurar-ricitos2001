def argoritmo_burbuja(lista):
    numero= len(lista)
    listafinal=lista
    for i in range (numero-1):
        for j in range(numero-1-i):
            if lista[j] > lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return listafinal

if __name__=="__main__":
    lista=[]
    elementos = int(input("introduce un numero: "))
    lista.append(elementos)
    while elementos:
        elementos = int(input("introduce un numero: "))
        lista.append(elementos)
    if elementos==0:
        listafinal=argoritmo_burbuja(lista)
        print(lista)