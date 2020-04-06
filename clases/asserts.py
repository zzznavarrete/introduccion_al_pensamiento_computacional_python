
"""
Asserts

 - Los asserts son un tipo de programación defensiva que nos permite asegurarnos que el usuario
   final tendrá un comportamiento determinado

"""

def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, f'No se permiten str vacíos'

        primeras_letras.append(palabra[0])

    return primeras_letras


if __name__ == "__main__":
    print(primera_letra("abc"))