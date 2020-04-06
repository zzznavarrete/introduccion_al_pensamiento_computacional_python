
def example_function(any):
    """ Description of our function

        example_paremeter int <-- any integer
        returns example_parameter + 5
    """
    return any + 5


if __name__ == "__main__":
    any = int(input('Ingrese cualquier número: '))
    print(example_function(any))
    print(help(example_function))