
"""
Diccionarios

 - Son como listas, pero en lugar de usar índices utilizan llaves.
 - No tienen orden interno.
 - Los diccionarios son mutables.
 - Pueden iterarse

"""

def diccionarios_ejemplos():
    # Definiendo un diccionario de edades, las claves serán nombres
    my_dict = {'Nicolas': 23, 'Chica': 9}
    # Imprimiendo el diccionario
    print(my_dict)
    # TRUCO: Por si queremos obtener el valor de una llave pero no estamos seguros de que exista
    #   podemos llamar a la llave con un parámetro opcional por si no la pilla
    print(my_dict.get('Xika', 999))
    
    # Podemos añadir elementos al diccionario
    my_dict['Rex'] = 13
    print(my_dict)

    # Eliminando un elemento via llave
    del my_dict['Rex']
    print(my_dict)

    # Iterando llaves de un diccionario
    for llave in my_dict.keys():
        print(llave)

    # Iterando valores de un diccionario
    for valor in my_dict.values():
        print(valor)
        
    # Iterando por la llave y el valor
    for llave, valor in my_dict.items():
        print(llave, valor)

    # También para saber si una llave está dentro del diccionario ocupamos la operación 'in'
    print('Chica' in my_dict)
    print('Tom' in my_dict)



if __name__ == "__main__":
    diccionarios_ejemplos()