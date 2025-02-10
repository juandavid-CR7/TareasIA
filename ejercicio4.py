def registrarProductos():
    productos = {}
    while True:
        nombre = input("Ingrese el nombre de un producto (o 'salir' para terminar): ")
        if nombre.lower() == "salir":
            break
        precio = float(input(f"Ingrese el precio de {nombre}: "))
        productos[nombre] = precio
        
        print(f"Producto agregado: {nombre} - Precio: {precio}")

    return productos
productos = registrarProductos()

print("Diccionario de productos:", productos)
