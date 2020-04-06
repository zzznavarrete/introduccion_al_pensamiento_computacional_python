
#Preguntar para activar el debug
debug = ''
while debug.upper() != 'Y' and debug.upper() != 'N':
    debug = input('¿Quieres activar el debug? [Y/n]: ')

objetivo = int(input('Escoge un número: '))

epsilon = 0.0001
bajo = 0.0
# La función max nos devuelve el máximo entre 2 valores
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo ) >= epsilon:
    if debug.upper() == 'Y':
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    respuesta = (alto + bajo) / 2

print(f'La raíz cuadrada de {objetivo} es {respuesta}')

