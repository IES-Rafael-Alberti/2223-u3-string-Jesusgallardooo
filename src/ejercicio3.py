''' Teniendo cierto código, Encapsúlalo en una función llamada cuenta, y hazla
    genérica de tal modo que pueda aceptar una cadena y una letra como argumentos.'''

def cuenta(cadena,letra):
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador = contador + 1
    return contador

if __name__ == "__main__":
    
    #Entrada
    palabra = input("Introduzca una cadena cualquiera --> ")
    caracter = input("Introduzca qué caracter quiere contar en dicha cadena: ")

    #Proceso
    resultado = cuenta(palabra, caracter)

    #Salida
    print("Su carácter se encuentra" + resultado + " veces en la palabra 'banana' ")