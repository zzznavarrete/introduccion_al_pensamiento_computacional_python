

if __name__ == "__main__":
    my_str = 'Platzi'
    #Saber el largo
    print(len(my_str))
    #Obteniendo la primera posición
    print(my_str[0])
    #Mostrado desde el 2do hasta el últmimo    
    print(my_str[2:])
    #Mostrando de la primera hasta -2 letras
    print(my_str[:-2])
    #Toda la cadena saltando de 2 en 2
    print(my_str[::2])
    #concetenando
    print('Yo estudio en '+ my_str)
    #Concatenando con llaves      
    print(f'Yo amo a {my_str}')
    #Imprimiendo un número N de veces
    print(f'Yo repito la palabra {my_str} 3 veces ' * 3)
