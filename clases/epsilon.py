# Preguntar si se quiere activar el debug
debug = ''
while debug.upper() != 'Y' and debug.upper() != 'N':
    debug = input('Quieres activar el debug? [Y/n]: ')


# Implementando algoritmo EPSILON, para aproximaciones
objetivo = int(input('Escoge un número: '))

dificultad = 0 
while dificultad != 1 and dificultad != 2 and dificultad != 3:
    dificultad = int(input('Escoge el nivel de precisión (Selecciona 1, 2 ó 3): [1] 0.01 - [2] 0.001 - [3] 0.003: '))

dificultad = '1'+('0'*dificultad)
epsilon = 0.1 / int(dificultad)
paso = epsilon**2
respuesta = 0.0


while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    if debug.upper() == 'Y':
        print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la raíz cuadrada de {objetivo}')
else:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')

