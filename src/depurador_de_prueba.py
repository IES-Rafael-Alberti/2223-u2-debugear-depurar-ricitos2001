#aleatorios (entre 1 y 100) y muestre el máximo y el mínimo, utilizando la función anterior.
#Por último, pide un número (entre 1 y 100) y el programa debe decir si está en la lista anterior.
import random
def CalcularMaxMin(lista):
    return (max(lista),min(lista))

if __name__=="__main__":
    numeros = []
    #Inicializo la lista con valores aleatorios
    for i in range(0,10):
        numeros.append(random.randint(1,1000))
        vmax,vmin = CalcularMaxMin (numeros)
        print("El valor máximo es",vmax)
        print("El valor mínimo es",vmin)
        numero = int(input("Dime un número del 1 al 100:"))
        while numero > 0 or numero < 100:
            print("El número debe estar entre 1 y 100")
            numero = int(input("Dime un número del 1 al 100:"))
            if numero in numeros:
                print("El número está en la lista")
            else:
                print("El número no está en la lista")