# Historial precio del producto 

# Diccionario para guardar los productos
productos = {}

# Preguntar cuántos productos se van a registrar
cantidad = int(input("¿Cuántos productos desea registrar?"))

# Ingreso de datos
for i in range(cantidad):
    print("\nProducto", i + 1)
    nombre = input("Ingrese el nombre del producto: ")
    precios = []

    # Pedir los 4 precios históricos 
    for j in range(4):
        precio = float(input("Ingrese el precio " + str(j + 1) + ": "))
        precios.append(precio)

    # Guardar como tupla
    productos[nombre] = tuple(precios)

print("\n----- RESULTADOS -----")

#  diccionario
for nombre, precios in productos.items():

    precio_alto = max(precios)
    precio_bajo = min(precios)
    promedio = sum(precios) / 4

    print("\nProducto:", nombre)
    print("Precio más alto:", precio_alto)
    print("Precio más bajo:", precio_bajo)
    print("Promedio:", promedio)

    # Comparar primer y último precio
    if precios[3] > precios[0]:
        print("El precio subió")
    elif precios[3] < precios[0]:
        print("El precio bajó")
    else:
        print("El precio se mantuvo igual")

# Mostrar productos con promedio mayor a  
print("\nProductos con promedio mayor a 500:")

for nombre, precios in productos.items():
    promedio = sum(precios) / 4
    if promedio > 500:
        print(nombre)