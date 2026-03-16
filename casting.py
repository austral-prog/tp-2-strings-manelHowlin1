def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    precio = int(input())
    descuento = float(input())
    cantidad =int(input())
    precio_descuento = (precio-descuento)
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")

    print(f"Precio con descuento: {precio_descuento}")

    total = precio_descuento * cantidad
    print("Total:",total)
    pass
