def argoritmo_burbuja(arreglo):
    numero = len(arreglo)
    for i in range(numero-1):
        intercambio = False
        for j in range(numero-1-i):
            if arreglo[j] > arreglo[j+1] :
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                intercambio = True
        if intercambio == False:
            listafinal=intercambio
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