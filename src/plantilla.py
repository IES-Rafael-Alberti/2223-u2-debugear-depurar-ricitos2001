#definicion del programa
def crear_funcion(funcion1,funcion2):
    funcion3=funcion1+funcion2
    funcion="la funcion es: "+str(funcion3)
    return funcion
if __name__=="__main__":
    #valores de la funcion
    funcion1=int(input("nombre de la primera funcion: "))
    funcion2=int(input("nombre de la segunda funcion: "))
    #funcion del programa
    funcion= crear_funcion (funcion1,funcion2)
    #resultado de la funcion
    print (funcion)