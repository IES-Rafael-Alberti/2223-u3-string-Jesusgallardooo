'''Escribe un bucle while que comience con el último carácter en la cadena y haga un
    recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra 
    en una línea independiente.'''


def Dar_La_Vuelta(cadena, contador, letras):
    while contador >= 0:
        letra = cadena[contador]
        letras.append(letra)
        contador = contador - 1
    return letra

if __name__ == "__main__":
    # Entrada
    cadena = input("Introduzca cualquier cadena: ")
    contador = len(cadena) - 1
    letras = []

    # Proceso
    Dar_La_Vuelta(cadena, contador, letras)

    #Salida
    for letra in letras:
        print(letra)
