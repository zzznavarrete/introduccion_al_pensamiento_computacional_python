
if __name__ == "__main__":
    #Pregutnando por un string
    pais = input('¿De qué país eres?: ')
    print('El tipo de dato es ' + str(type(pais)))
    #Preguntando por un int
    edad = int(input('Escribe tu edad: '))
    print('El tipo de dato es ' + str(type(edad)))
    #Preguntar el nombre del usuario y que devuelva el nombre como saludo y el largo de la cadena
    print('*** Reto ***')
    nombre = input('¿Cuál es tu nombre?: ')
    print("Hola! "+ nombre + ", el largo de tu nombre es de " + str(len(nombre)) + ' caracteres')

    pass