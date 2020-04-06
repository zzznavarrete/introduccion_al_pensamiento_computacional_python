"""
Listas

 - Son secuencias de objetos, pero a diferencia de las tuplas, sí son mutables
 - Es posible iterar con ellas
 - Cuando le asignas una lista existente a una nueva variable, esta en realidad es un 
  espejo de la primera lista, por lo que, en vez de asignar, se debe clonar la primera lista.


"""

def listas_ejemplo():
    print('**** Listas Ejemplos ****')
    # Declarando una lista 
    my_list = [1,2,3]
    # Imprimiendo la primera posición de la lista
    print(my_list[0])
    # Imprimiendo desde la segunda posición hasta todo lo que quede
    print(my_list[1:])
    # Reemplazando el primer valor de la lista
    my_list[0]  = 'a'
    print(my_list)
    # .pop() elimina el último elemento (retorna el valor que eliminó)
    print(my_list.pop())
    print(my_list)



def clonar_list():
    print('**** Lista clonación ****')
    a = [1,2,3]
    b = a
    print("Imprimimos la posición de memoria de A y B para verificar que es la misma")
    print(id(a), id(b))
    print('Para evitar esto utilizamos la clonación entre listas')
    # Clonamos la lista a en la lista c 
    c = list(a)
    print('Ahora, aunque las 3 listas tengan los mismos valores')
    print(a,b,c)
    print('La última tiene una posición en memoria distinta')
    print(id(a), id(b), id(c))



"""
List Comprenhension

 - Es una forma concisa de aplicar operaciones a los valores de una secuencia
 - También se pueden aplicar condiciones para filtrar
"""

def list_comprenhension():
    print('**** List Comprenhension ****')
    # Generando una lista del 0 al 99
    my_list = list(range(100))
    print(my_list)
    # Creando una lista que tenga el doble de cada valor en la primera lista
    my_list_double = [ i* 2 for i in my_list]
    print(my_list_double)
    # Sacando sólo los valores pares dentro de nuestra lista
    my_list_pair = [ i for i in my_list if i % 2 == 0 ]
    print(my_list_pair)


if __name__ == "__main__":
    listas_ejemplo()
    clonar_list()
    list_comprenhension()
    
