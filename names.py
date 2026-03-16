def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    nombre = input()
    apellido = input()

    nombre_minusculas = nombre.lower() + " " + apellido.lower()
    nombre_titulo = nombre.title() + " " + apellido.title()
    nombre_mayusculas = nombre.upper() + " " + apellido.upper()

    print(nombre_minusculas)
    print(nombre_titulo)
    print(nombre_mayusculas)
    print(f"\t{nombre_minusculas}")

    pass
