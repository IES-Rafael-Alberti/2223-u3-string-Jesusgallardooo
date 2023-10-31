


def contar_caracter(cadena, caracter):
    respuesta = cadena.count(caracter)
    return respuesta

if __name__ == "__main__":
    #Entrada
    cadena = "banana"
    caracter = input("Introduzca qué carácter desea contar en la palabra banana: ")

    #Proceso
    resultado = contar_caracter(cadena, caracter)

    #Salida
    print(resultado)

