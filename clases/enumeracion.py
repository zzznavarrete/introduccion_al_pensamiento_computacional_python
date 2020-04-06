
#Tratar de determinar si un número tiene una raíz cuadrada exacta
objetivo = int(input('Escoje un entero: '))
respuesta = 0

#El **2 es para elevar al cuadrado un número
while respuesta**2 < objetivo:
    respuesta += 1

if respuesta** 2 == objetivo:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene raíz cuadrada exacta')