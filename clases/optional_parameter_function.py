

def nombre_completo(nombre, apellido, inverso=False):
    if inverso:
        return apellido + ', ' + nombre
    else:
        return nombre + ', ' + apellido


var_nombre = 'Nicolás'
var_apellido = 'Neira'
#Sin pasarle el valor opcional
print(nombre_completo(var_nombre, var_apellido))
#Pasándole el valor opcional
print(nombre_completo(var_nombre, var_apellido, True))
#Llámando la función con keywords
print(nombre_completo(nombre=var_nombre, apellido=var_apellido))
