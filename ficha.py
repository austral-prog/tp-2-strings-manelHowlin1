def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    nombre_completo = input("Nombre: ").strip().title()
    mail = input("Email: ").lower()
    nota1 = int(input())
    nota2 = int(input())
    nota3 = int(input())

    print("========================")
    print("    FICHA DEL ALUMNO")
    print("========================")
    print(f"Nombre: {nombre_completo.title()}")
    print(f"Email: {mail}")
    print(f"Caracteres en nombre: {len(nombre_completo)}")
    print(f"Iniciales: {nombre_completo[0]}{nombre_completo[nombre_completo.find(' ')+1]}")
    print(f"Usuario: {nombre_completo[nombre_completo.find(' ')+1:].lower()}.{nombre_completo[:nombre_completo.find(' ')].lower()}")
    print(f"Email valido: {'@' in mail}")
    print(f"Dominio: {mail[mail.find('@')+1:]}")
    print(f"Nombre para archivo: {nombre_completo.replace(' ','_')}")
    print(f"Cantidad de a: {(nombre_completo.lower()).count('a')}")
    print(f"Codigo secreto: {nombre_completo[::-1].upper()}")
    print(f"Nota 1: {nota1}\nNota 2: {nota2}\nNota 3: {nota3}")
    print(f"Suma: {nota1 + nota2 + nota3}")
    print(f"Promedio: {(nota1 + nota2 + nota3)/3}")
    print(f"Promedio entero: {(nota1 + nota2 + nota3)//3}")
    print("========================")

