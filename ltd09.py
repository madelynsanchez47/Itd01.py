#lista vacia donde se guardaran los productos
productos = []
total = 0 #variable donde se almacenara el total del inventario

#preguntamos la cantidad de productos a ingresar
n = int(input("¿Cuantos productos desea ingresar?"))

#leemos cada producto y lo guardamos en una lista de diccionarios
for i in range(n):
    print(f"\nProducto {i+1}:")
    nombre = input("Nombre:")
    precio = float(input("Precio:"))
    cantidad = int(input("Cantidad"))
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

    #calculamos el total del inventario
    total += precio * cantidad

    #Mostramos los productos con cantidades menores a 10
    print("Productos con cantidades menores que 10:")
    for i in range(n):
        if productos[i]["cantidad"]< 10:
            print(productos[i])

    print(f"\nTotal del inventario: {total}")