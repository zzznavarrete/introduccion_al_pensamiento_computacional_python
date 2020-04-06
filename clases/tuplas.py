
""" Tuplas

- Son secuencias inmiutables de objetos.
- A diferencia de las cadenas, pueden contener cualquier tipo de dato.
- Pueden utilizarse para devolver varios valores en una función.

"""

if __name__ == "__main__":
    my_tuple = ()
    print(str(type(my_tuple)))
    # Las tuplas pueden contener cualquier tipo de variable juntos
    my_tuple = (1, 'dos', True)

    # Imprimimos el valor de una tupla según su posición 
    print(my_tuple[0])

    # Si ejecutaramos la instrucción de abajo daría error ya que las tuplas no se pueden modificar.
    #my_tuple[0] = 2

    # Para asignar una tupla con el largo de 1 debemos hacer lo siguiente
    my_tuple_1_length = (1,)

    # Ahora creamos otra tupla
    my_other_tuple = (2,3,4)

    # A pesar de que no podemos modificar tuplas, si podemos reasignar
    my_tuple += my_other_tuple
    print(my_tuple)

    #También podemos asignar variables según la posición de la tupla
    x, y, z = my_other_tuple
    print(x, y, z)

    pass