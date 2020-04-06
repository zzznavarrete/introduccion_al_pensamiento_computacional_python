
"""
Filosofía de programación en python.

 - En python se suele programar bajo el dictamen EAFP (Easier to ask for forgiveness than permission)
    en español, "Es más fácil pedir perdón que permiso", esto quiere decir que se accede o ejecutan
    métodos sin tener la total certeza de que estos lanzarán una excepción, y es por eso que se programa 
    bajo esa lógica al incluir las excepciones.

- En otros lenguajes de programación como por ej, JS, está la filosofía LBYL (Look before you leap)
    en español, 'Revisa antes de saltar'. Por lo que se consulta antes de ejecutar o acceder a ciertos
    métodos o funciones.

"""

# Python
def busca_pais(paises, pais):
    """
    Paises es un diccionario. Pais es la llave.
    Codigo con el principio EAFP.
    """
    
    try:
        return paises[pais]
    except KeyError:
        return None



"""
 JS
/**
* Paises es un objeto. Pais es la llave.
* Codigo con el principio LBYL.
*/
function buscaPais(paises, pais) {
  if(!Object.keys(paises).includes(pais)) {
    return null;
  }

  return paises[pais];
}
"""