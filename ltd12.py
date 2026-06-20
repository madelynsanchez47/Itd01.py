#lista donde se guardaran los productos del carrito
carrito = []

total = 0

#preguntamos cuantos productos desea agregar
n = int(input("¿Cuantos productos desea agregar al carrito?"))

#leemos los productos
for i in range(n):
    print(f"\nProducto {i+1}:")

    nombre = input("Nombre:")
    precio = float(input("Precio unitario:"))
    cantidad = int(input("Cantidad:"))

    carrito.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })

#mostrar ticket
print("\nTicket de compra:")

#ordenamos de mayor a menor por precio
carrito.sort(key=lambda x: x["precio"], reverse=True)

for i in range(n):
    subtotal = carrito[i]["precio"] * carrito[i]["cantidad"]
    total += subtotal

    print(f"\nProducto: {carrito[i]['nombre']}")
    print(f"Precio: {carrito[i]['precio']}")
    print(f"Cantidad: {carrito[i]['cantidad']}")
    print(f"Subtotal: {subtotal}")

#aplicar descuento
if total > 50:
    descuento = total * 0.15
    total = total - descuento

    print(f"\nDescuento aplicado: {descuento}")

print(f"\nTotal general: {total}")