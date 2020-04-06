"""
Rangos.

 - Representan una secuencia de números enteros.
 - range(comienzo, fin, pasos)
 - Al igual que las cadens y las tuplas, los rangos son inmutables.
 - Muy eficientes en uso de memoria y normalmente utilizando for loops.

"""


if __name__ == "__main__":
    # Declarando un rango
    my_range = range(1,5)
    # Viendo el tipo de objeto
    print(str(type(my_range)))
    # Imprimiendo los valores de dentro
    for i in my_range:
        print(i)

    print('*'*10)

    # Declarando un rango con pasos
    my_range = range(0,7,2)
    for i in my_range: 
        print(i)
